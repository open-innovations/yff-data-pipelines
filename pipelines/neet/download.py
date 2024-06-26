import os
import re
from lib.scraper import get_links
from lib.downloader import download_url_to_file as download_file
from lib.util import set_working_directory

NEET_PAGE = 'https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment/datasets/youngpeoplenotineducationemploymentortrainingneettable1'

def download_neet():
    TARGET_DIR = os.path.dirname(__file__) + '/../../data/raw/'
    # Make sure that the target exists

    with set_working_directory(TARGET_DIR):
        suffix = '.xlsx'
        latest = get_links(NEET_PAGE, href=re.compile(f'{suffix}$'))[0]
        filename = 'neet-latest.xlsx'
        download_file(latest, filename)


if __name__ == '__main__':
    download_neet()
