import re
from .date import isodate
import petl as etl
from petl import dateparser


def infer_freq(rec, date_field='date'):
    if re.match(r'^\d{4}\s+Q', rec[date_field]):
        return 'q'
    if re.match(r'^\d{4}\s+[A-Z]{3}$', rec[date_field]):
        return 'm'
    if re.match(r'^\d{4}$', rec[date_field]):
        return 'a'


def parse_quarter(date):
    [y, q] = re.split(r'\sQ', date)
    quarter = f"{y}-{int(q) * 3 - 2:02}-01"
    return isodate(quarter)


def find_header_length(file):
    labels = etl.fromcsv(file, header=['title']).values('title')
    return (
      labels.index('Important Notes'),
      labels.index('CDID')
    )


def metadata(file):
    header_length, cdid_row = find_header_length(file)
    metadata = (
      etl.fromcsv(file)
        .rowslice(header_length)
        .transpose()
        .movefield('CDID', 0)
        .convert('Release Date', dateparser('%d-%m-%Y'))
        .convert('Next release', dateparser('%d %B %Y'))
    )
    return metadata


def transform(file):
    header_length, cdid_row = find_header_length(file) 
    return (
      etl.fromcsv(file)
        .skip(cdid_row)
        .rowslice(header_length - cdid_row, None)
        .rename('CDID', 'date')
        .addfield('freq', infer_freq, index=1)
        .convert('date', dateparser('%Y'), where=lambda x: x['freq'] == 'a')
        .convert('date', parse_quarter, where=lambda x: x['freq'] == 'q')
        .convert('date', dateparser('%Y %b'), where=lambda x: x['freq'] == 'm')
        .melt(key=['date', 'freq'])
        .convert('value', float)
        .selectnotnone('value')
        .sort(key=['date', 'variable', 'freq'])
    )
