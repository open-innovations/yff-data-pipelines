import os
import re
from lib.scraper import get_links, download_file
from lib.util import set_working_directory

SOURCE_PAGE = 'https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/x10adjustedemploymentunemploymentandeconomicinactivity'

def download_x10():
    TARGET_DIR = os.path.dirname(__file__) + '/../../data/raw/'
    # Make sure that the target exists

    with set_working_directory(TARGET_DIR):
        suffix = '.xlsx'
        latest = get_links(SOURCE_PAGE, href=re.compile(f'{suffix}$'))[0]
        filename = 'x10.xlsx'
        download_file(latest, filename)


if __name__ == '__main__':
    download_x10()
