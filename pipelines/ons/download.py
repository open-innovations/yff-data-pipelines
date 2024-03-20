import os
import sys
from lib.etl.sources import download_file


if __name__ == '__main__':
    (key, url) = sys.argv[1:]
    
    RAW_CSV = os.path.abspath(f'{os.path.dirname(__file__)}/../../data/raw/{key}.csv')
    os.makedirs(os.path.dirname(RAW_CSV), exist_ok=True)

    download_file(url, RAW_CSV)
