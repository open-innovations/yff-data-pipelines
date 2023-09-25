import hashlib
import requests
import pandas as pd

def md5_for_webpage(url, block_size=2**20):
    md5 = hashlib.md5()
    r = requests.get(url, stream=True)
    for chunk in r.iter_content(chunk_size=block_size):
        md5.update(chunk)
    return md5.hexdigest()
  
if __name__ == '__main__':
    with open('pages-to-monitor.txt') as f:
        pages = [l.strip() for l in f.readlines()]

    pd.DataFrame([ (page, md5_for_webpage(page)) for page in pages ], columns=['url', 'hash']).sort_values('url').to_csv('control.csv', index=False)