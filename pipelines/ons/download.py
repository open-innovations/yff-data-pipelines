import os
import sys
import requests


if __name__ == '__main__':
    (key, url) = sys.argv[1:]
    
    RAW_CSV = os.path.abspath(f'{os.path.dirname(__file__)}/../../data/raw/{key}.csv')
    os.makedirs(os.path.dirname(RAW_CSV), exist_ok=True)

    r = requests.get(url)
    with open(RAW_CSV, 'wb') as f:
        f.write(r.content)