from re import compile
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import requests


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def get_filename(url, pattern, index=0):
    url = urlparse(url)
    req = Request(url.geturl(),
                  headers={
                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0",
    })
    with urlopen(req) as site:
        html = site.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

    links = [l['href'] for l in soup.find_all(href=compile(pattern))]
    file_link = url._replace(path=links[index])
    return file_link.geturl()


def get_link_by_text(url, pattern):
    url = urlparse(url)
    req = Request(url.geturl(),
                  headers={
                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0",
    })
    with urlopen(req) as site:
        html = site.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

    links = [l['href'] for l in soup.find_all('a', text=compile(pattern))]
    file_link = url._replace(path=links[0])
    return file_link.geturl()


def download_latest(link, file, pattern='.xlsx{0,1}$', index=0):
    url = get_filename(link, pattern=pattern, index=index)
    download_file(url, file)
