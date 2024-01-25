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
        # Download LFS data
        download_url_to_file(
          'https://stats.oecd.org/SDMX-JSON/data/LFS_D/AUS+AUT+BEL+CAN+CHL+COL+CRI+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+OECD.MEN+WOMEN+MW.1564+1519+1524+2024+2064+2529+2534+2539+2554+2564+3034+3039+3539+3544+4044+4049+4549+4554+5054+5059+5559+5564+6064+6099+6569+6599+7074+7099+7599+7579+8099+900000.E+L+P+U.A/all?startTime=2010&endTime=2022&dimensionAtObservation=allDimensions&contentType=csv',
          local_file='lfs_by_sex_and_age.csv'
        )
        
        # Download employment rate data
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