import petl as etl
from pathlib import Path

RAW = Path('../../data/raw/oecd');
OUT = Path('../../data/processed/oecd/')

neet = (
  etl
    .fromcsv(
        RAW / 'neet.csv'
    )
    .cut(
        'REF_AREA',
        'MEASURE',
        'POP_GROUP',
        'UNIT_MEASURE',
        'TIME_PERIOD',
        'OBS_VALUE'
    )
    .addfield(
        'FREQUENCY',
        'A',
        index=4
    )
    .convert(
      'OBS_VALUE', float
    )
    .sort(
        ['REF_AREA', 'TIME_PERIOD']
    )
)

neet.tocsv( OUT / 'neet.csv')