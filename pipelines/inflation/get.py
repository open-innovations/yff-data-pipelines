import os
import requests


if __name__ == '__main__':
    url = 'https://www.ons.gov.uk/file?uri=/economy/inflationandpriceindices/datasets/consumerpriceindices/current/mm23.csv'
    filename = f'{os.path.dirname(__file__)}/../../data/raw/mm23.csv'
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
