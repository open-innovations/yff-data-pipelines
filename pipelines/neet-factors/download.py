import os
import requests
from pathlib import Path
from urllib.parse import urlparse


def download_url_to_file(url, local_file=None):
    if not local_file:
        local_file = filename_from_url(url)
    r = requests.get(url)
    with open(local_file, 'wb') as f:
        f.write(r.content)


def filename_from_url(url) -> str:
    return Path(
        urlparse(url).path
    ).name


def main():
    # https://www.gov.uk/government/statistics/children-in-low-income-families-local-area-statistics-2014-to-2022
    download_url_to_file(
        url='https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1145380/children-in-low-income-families-local-area-statistics-2014-to-2022.ods',
    )


if __name__ == "__main__":
    ROOT_DIR = Path(__file__).parent.joinpath(
        '../../data/raw/neet-factors').resolve()
    ROOT_DIR.mkdir(parents=True, exist_ok=True)
    os.chdir(ROOT_DIR)

    main()
