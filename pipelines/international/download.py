'''
Need to ensure that PYTHONPATH includes the root directory of the repo, so that it can resolve the lib

If located in the root directory, run the following:

    PYTHONPATH=. python pipelines/international/download.py
'''
import logging
from pathlib import Path

from lib.downloader import download_url_to_file

logging.basicConfig(level=logging.INFO)


def download():
    '''
    Create working directory, then download a series of datasets into it.
    '''
    # Set up output directory
    output_dir = Path(__file__).parent.joinpath(
        '../../data/raw/oecd').resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Download LFS data
    download_url_to_file(
        # 'https://stats.oecd.org/SDMX-JSON/data/LFS_D/AUS+AUT+BEL+CAN+CHL+COL+CRI+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+OECD.MEN+WOMEN+MW.1564+1519+1524+2024+2064+2529+2534+2539+2554+2564+3034+3039+3539+3544+4044+4049+4549+4554+5054+5059+5559+5564+6064+6099+6569+6599+7074+7099+7599+7579+8099+900000.E+L+P+U.A/all?startTime=2010&endTime=2022&dimensionAtObservation=allDimensions&contentType=csv',
        'https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_INDIC,1.0/.OLF_WAP+UNE_LF+EMP_WAP+LF_WAP...Y....A?startPeriod=2010&dimensionAtObservation=AllDimensions&format=csvfilewithlabels',
        local_file=output_dir / 'lfs_by_sex_and_age.csv'
    )

    # Download NEET
    # https://data-explorer.oecd.org/vis?tm=neet&pg=0&snb=3&vw=tb&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_CWB%40DF_CWB&df%5Bag%5D=OECD.WISE.CWB&df%5Bvs%5D=1.0&dq=.A3_5.&lom=LASTNOBSERVATIONS&lo=5&pd=1997%2C&to%5BTIME_PERIOD%5D=false
    download_url_to_file(
        # 'https://stats.oecd.org/sdmx-json/data/DP_LIVE/.NEET.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en',
        'https://sdmx.oecd.org/archive/rest/data/OECD,DF_DP_LIVE,/.NEET.15_29_WOMEN+15_29_MEN+15_29..A?startPeriod=1950&endPeriod=2022&dimensionAtObservation=AllDimensions&format=csvfilewithlabels',
        local_file=output_dir / 'neet.csv'
    )

    # Download wage levels
    # This is measures Low pay incidence and high pay incidence for all countries dating back to 1970
    # https://data-explorer.oecd.org/vis?tm=pay&pg=0&snb=64&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_EARNINGS%40PAY_INCIDENCE&df%5Bag%5D=OECD.ELS.SAE&df%5Bvs%5D=1.0&dq=.HP_I%2BLP_I....._T&pd=1970%2C&to%5BTIME_PERIOD%5D=false
    download_url_to_file(
        # 'https://stats.oecd.org/sdmx-json/data/DP_LIVE/.WAGELEVEL.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en',
        'https://sdmx.oecd.org/public/rest/data/OECD.ELS.SAE,DSD_EARNINGS@PAY_INCIDENCE,1.0/.HP_I+LP_I.....M+F+_T?startPeriod=1970&dimensionAtObservation=AllDimensions&format=csvfilewithlabels',
        local_file=output_dir / 'wage_levels.csv'
    )


if __name__ == '__main__':
    download()
