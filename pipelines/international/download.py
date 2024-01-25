'''
PYTHONPATH=. python pipelines/international/download.py

Need to ensure that PYTHONPATH includes the root directory of the repo, so that it can resolve the lib
'''
from pathlib import Path
from lib.downloader import download_url_to_file
from lib.util import set_working_directory


def download():
    '''
    Create working directory, then download a series of datasets into it.
    '''
    # Set up output directory
    output_dir=Path(__file__).parent.joinpath('../../data/raw/oecd').resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Set the current working directory
    with set_working_directory(output_dir):
        # Download 
        download_url_to_file(
          'https://stats.oecd.org/sdmx-json/data/DP_LIVE/.EMPAGE.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en',
          local_file='employment_rate_by_age_group.csv'
        )

        # Download NEET
        download_url_to_file(
          'https://stats.oecd.org/sdmx-json/data/DP_LIVE/.NEET.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en',
          local_file='neet.csv'
        )

        download_url_to_file(
          'https://stats.oecd.org/sdmx-json/data/DP_LIVE/.WAGELEVEL.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en',
          local_file='wage_levels.csv'
        )


if __name__ == '__main__':
    download()