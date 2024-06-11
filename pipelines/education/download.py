import logging
import re
from pathlib import Path

from lib.util import set_working_directory
from lib.scraper import get_links
from lib.downloader import download_url_to_file

logging.basicConfig(
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def download():
    raw_data = Path(__file__).parent.joinpath('../../data/raw/education')
    raw_data.mkdir(parents=True, exist_ok=True)
    
    with set_working_directory(raw_data):
        # Get KS4 performance data
        links = get_links(
            'https://explore-education-statistics.service.gov.uk/find-statistics/key-stage-4-performance',
            string=re.compile(r'Download all data \(zip\)')
        )
        logging.info("Links: %s", links)
        download_url_to_file(
            links[0],
            local_file='key-stage-4-performance.zip'
        )

        # Get 16-18 destinations data
        links = get_links(
            'https://explore-education-statistics.service.gov.uk/find-statistics/16-18-destination-measures',
            string=re.compile(r'Download all data \(zip\)')
        )
        download_url_to_file(
            links[0],
            local_file='16-18-destination-measures.zip'
        )

    
if __name__ == '__main__':
    download()