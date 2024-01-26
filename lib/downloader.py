import requests
from pathlib import Path
from urllib.parse import urlparse


def download_url_to_file(url, local_file=None):
    '''
    Download a url to a local file.
    If `local_file` is not provided, attempts to work it out from the url.
    '''
    if not local_file:
        local_file = filename_from_url(url)
        
    with requests.get(url, stream=True) as r, open(local_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=None):
            fd.write(chunk)


def filename_from_url(url) -> str:
    return Path(
        urlparse(url).path
    ).name
