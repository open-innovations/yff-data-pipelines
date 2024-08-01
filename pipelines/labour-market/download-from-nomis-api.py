import os
from time import sleep
import pandas as pd
import http.client
import logging

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__file__)

# To get these, use the 'select areas within'
geo_pcon_2010=','.join(str(i) for i in range(1929379841, 1929380473))  # This excludes Northern Ireland
geo_pcon_2024=','.join(str(i) for i in range(721420289, 721420939))
geographies=','.join([geo_pcon_2010, geo_pcon_2024])

def chunk(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

geo_batches = [','.join(g) for g in chunk(geographies.split(','), 400)]

date_range='latestMINUS12-latest'

variables = [
  18, 19, 20,
  83, 84, 85, 86,
  110, 111, 112, 113,
  1213,
  1219,
  1493
]

def get_variable(variable, geography):
    url = f'https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5.data.csv?geography={geography}&date={date_range}&variable={variable}&measures=20599,21001,21002,21003'
    retries = 3
    while retries > 0:
        try:
            data = pd.read_csv(url)
            retries = 0
        except http.client.RemoteDisconnected as e:
            retries -= 1
            if retries <=0:
                raise e
            sleep(5)

    if data.index.size == 25000:
        raise RuntimeError('Maxed out request to NOMIS (%d rows)', data.index.size)
    return data

if __name__ == '__main__':
    THIS_DIR = os.path.dirname(__file__)
    print(THIS_DIR)

    results = [
        get_variable(variable=v, geography=g) for v in variables for g in geo_batches
    ]
    data = pd.concat(results,
        axis=0
    )
    
    DATA_FILE=f'{THIS_DIR}/../../data/raw/lfs_by_pcon.csv'
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    data.reset_index().to_csv(DATA_FILE, index=False)