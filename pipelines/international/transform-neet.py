import petl as etl
from pathlib import Path

RAW = Path('../../data/raw/oecd')
OUT = Path('../../data/processed/oecd/')

neet = (
  etl
    .fromcsv(
        RAW / 'neet.csv'
    )
    .cut(
        'LOCATION',
        'INDICATOR',
        'SUBJECT',
        'Subject',
        'MEASURE',
        'FREQUENCY',
        'TIME_PERIOD',
        'OBS_VALUE'
    )
    .convert(
      'OBS_VALUE', float
    )
    .sort(
        ['TIME_PERIOD', 'LOCATION']
    )
)

neet.tocsv( OUT / 'neet.csv')