from pathlib import Path

import petl as etl

RAW = Path('../../data/raw/oecd')
OUT = Path('../../data/processed/oecd')

wage_levels = etl.fromcsv( RAW / 'wage_levels.csv' )

(
    wage_levels
        .cut(
            'REF_AREA',
            'STRUCTURE_NAME',
            'MEASURE',
            'UNIT_MEASURE',
            'TIME_PERIOD',
            'OBS_VALUE'
        )
        .addfield(
            'FREQUENCY',
            'A',
            index=4
        )
        .sort(
            ['REF_AREA', 'TIME_PERIOD']
        )
        .tocsv(OUT / 'wage_levels.csv')
)