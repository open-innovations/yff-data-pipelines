import os
import requests


if __name__ == '__main__':
    url = 'https://www.ons.gov.uk/file?uri=/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/labourmarketstatistics/current/lms.csv'
    filename = f'{os.path.dirname(__file__)}/../../data/raw/lms.csv'
    print(filename)
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
