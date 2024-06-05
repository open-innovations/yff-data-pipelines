import logging
from pathlib import Path
from time import sleep
from urllib.parse import urlparse

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def download_url_to_file(url, local_file=None, retries=3, backoff=10):
    '''
    Download a url to a local file.
    If `local_file` is not provided, attempts to work it out from the url.
    '''
    if not local_file:
        local_file = filename_from_url(url)

    while (retries > 0):
        try:
            logger.info("Downloading %s", local_file)
            with requests.get(url, stream=True) as r, open(local_file, 'wb') as fd:
                assert r.status_code == 200, r.status_code
                for chunk in r.iter_content(chunk_size=None):
                    fd.write(chunk)
            retries = 0
        except AssertionError as e:
            logger.warn('Download failed with status code %s', url, e)
            sleep(backoff)
            retries -= 1


def filename_from_url(url) -> str:
    return Path(
        urlparse(url).path
    ).name
