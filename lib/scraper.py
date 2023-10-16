import requests
import urllib.parse
from bs4 import BeautifulSoup


def get_links(url, *args, **kwargs):
    """
    Search in a web page for arbitrary items.
    The url argument is required, everything else is passed to a Beautiful Soup find call.
    """
    referrer = urllib.parse.urlparse(url)

    def canonical(link):
        u = urllib.parse.urlparse(link, scheme=referrer.scheme)
        if u.netloc == '':
            u = u._replace(netloc=referrer.netloc)
        return u.geturl()

    links = BeautifulSoup(
        requests.get(url).text,
        features="html.parser"
    ).find_all(
        'a', *args, **kwargs
    )

    return [canonical(l['href']) for l in links]


def download_file(url, file):
    r = requests.get(url)
    with open(file, 'wb') as f:
        f.write(r.content)