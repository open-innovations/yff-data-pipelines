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
    # Children in Low Income Families
    # https://www.gov.uk/government/statistics/children-in-low-income-families-local-area-statistics-2014-to-2022
    # Note: collection homepage is https://www.gov.uk/government/collections/children-in-low-income-families-local-area-statistics
    # This is currently latest release
    download_url_to_file(
        url='https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1145380/children-in-low-income-families-local-area-statistics-2014-to-2022.ods',
    )

    # Children looked after
    # https://explore-education-statistics.service.gov.uk/find-statistics/children-looked-after-in-england-including-adoptions
    # Note: below is not most recent dataset.
    # https://content.explore-education-statistics.service.gov.uk/api/releases/0832e5e1-7b1e-433d-bcf6-cafc10d635e5/files?fileIds=42de6f1b-cdab-4151-1fe6-08dac160aa64
    download_url_to_file(
        url='https://content.explore-education-statistics.service.gov.uk/api/releases/0832e5e1-7b1e-433d-bcf6-cafc10d635e5/files',
        local_file='cla-all.zip'
    )

    # Disability (age < 25)
    # https://www.ons.gov.uk/datasets/create/filter-outputs/dad776cf-f624-46b6-8628-629170a262b9#get-data
    # Note: based on Census 2021
    download_url_to_file(
        url='https://www.ons.gov.uk/datasets/create/filter-outputs/dad776cf-f624-46b6-8628-629170a262b9?f=get-data&format=csv',
        local_file='health_disability_2021.csv'
    )

    # Disability (all)
    # https://www.ons.gov.uk/datasets/TS038ASP/editions/2021/versions/2/filter-outputs/0e832fd8-107d-4020-abc9-09ca0d87911f#get-data
    # Note: based on Census 2021
    download_url_to_file(
        url='https://www.ons.gov.uk/datasets/TS038ASP/editions/2021/versions/2/filter-outputs/d69f4719-2717-4a57-9f3f-db2587ba8e2a?f=get-data&format=csv',
        local_file='family_disability_2021.csv'
    )

    # Economic inactivity (NEET)
    # https://www.ons.gov.uk/datasets/create/filter-outputs/6c4e9576-045d-4e31-a87a-a84aab44a0fe#get-data
    download_url_to_file(    
        url='https://www.ons.gov.uk/datasets/create/filter-outputs/10dec042-ca27-448a-9e63-2e0ab12c1d6f?f=get-data&format=csv',
        local_file='economic_inactivity_status.csv'
    )

    # Fertility rates (age < 20)
    # Fertility rates (age 20-24)
    # https://www.nomisweb.co.uk/datasets/lebirthrates
    # https://www.nomisweb.co.uk/Query/GetFile?filename=4109319377568812.csv
    download_url_to_file(
        url='https://www.nomisweb.co.uk/api/v01/dataset/NM_207_1.data.csv?geography=1811939329...1811939332,1811939334...1811939336,1811939338...1811939428,1811939436...1811939442,1811939768,1811939769,1811939443...1811939497,1811939499...1811939501,1811939503,1811939505...1811939507,1811939509...1811939517,1811939519,1811939520,1811939524...1811939570,1811939575...1811939599,1811939601...1811939628,1811939630...1811939634,1811939636...1811939647,1811939649,1811939655...1811939664,1811939667...1811939680,1811939682,1811939683,1811939685,1811939687...1811939692&date=latest&measure=5,6&measures=20100',
        local_file='fertility_rates.csv'
    )

    # IMD Crime
    # IMD Health
    # https://assets.publishing.service.gov.uk/media/5d8b3cfbe5274a08be69aa91/File_10_-_IoD2019_Local_Authority_District_Summaries__lower-tier__.xlsx
    download_url_to_file(
        url='https://assets.publishing.service.gov.uk/media/5d8b3cfbe5274a08be69aa91/File_10_-_IoD2019_Local_Authority_District_Summaries__lower-tier__.xlsx'
    )

    # Lone parent households
    # https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/families/adhocs/13586estimatednumberofhouseholdsbyselectedhouseholdtypeslocalauthoritiesinenglandandwalescountiesandregionsofenglandscottishcouncilareasandgreatbritainconstituentcountries2004to2019
    download_url_to_file(
        url='https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/birthsdeathsandmarriages/families/adhocs/13586estimatednumberofhouseholdsbyselectedhouseholdtypeslocalauthoritiesinenglandandwalescountiesandregionsofenglandscottishcouncilareasandgreatbritainconstituentcountries2004to2019/aps2004to2019finalv2.xlsx',
        local_file='aps2004to2019finalv2.xlsx'
    )

    # Pupils with SEN support
    # https://explore-education-statistics.service.gov.uk/data-tables/fast-track/2522256d-6975-4d8b-aad4-3e5310e4ebe8
    # https://explore-education-statistics.service.gov.uk/data-tables/permalink/b56bb8ce-90bb-4e46-af62-08dbfa4e7cea
    download_url_to_file(
        url='https://content.explore-education-statistics.service.gov.uk/api/releases/77bc898f-948d-4080-b092-3ebc3eb1e0a5/files',
        local_file='special-educational-needs-in-england_2022-23.zip'
    )

    # Qualification below level 2 (age 16-24)
    # https://www.ons.gov.uk/datasets/create/filter-outputs/34f71c2b-2c63-411d-8778-5be794881875#get-data
    download_url_to_file(
        url='https://www.ons.gov.uk/datasets/create/filter-outputs/34f71c2b-2c63-411d-8778-5be794881875?f=get-data&format=csv',
        local_file='qualifications_below_level_2.csv'
    )

    # Qualification below level 2 (all)
    # https://www.ons.gov.uk/peoplepopulationandcommunity/educationandchildcare/bulletins/educationenglandandwales/census2021
    # AS ABOVE???

    # School Absences
    # https://explore-education-statistics.service.gov.uk/find-statistics/pupil-absence-in-schools-in-england/data-guidance
    download_url_to_file(
        url='https://content.explore-education-statistics.service.gov.uk/api/releases/a1a18ca2-800b-4457-50ea-08dbb9a6ec1c/files?fileIds=51b6d93f-f6be-4745-8a61-08dbca41c45d',
        local_file='school_absence_by_geographic_area.zip'
    )

    # School Exclusions
    # School Suspensions
    # https://explore-education-statistics.service.gov.uk/find-statistics/permanent-and-fixed-period-exclusions-in-england#explore-data-and-files
    download_url_to_file(
        url='https://content.explore-education-statistics.service.gov.uk/api/releases/dc547ce0-9486-4862-fd0e-08dbd13dc3fc/files',
        local_file='exclusions_and_suspensions.zip'
    )

    # Socially renting households
    # https://www.ons.gov.uk/datasets/TS054/editions/2021/versions/4
    download_url_to_file(
        url='https://www.ons.gov.uk/datasets/TS054/editions/2021/versions/4?f=get-data&format=csv',
        local_file='socially_renting_households.csv'
    )

    # Unpaid carer (age 16-24)
    # https://www.ons.gov.uk/filters/a10ac0de-d525-453b-9848-e567af338a91/dimensions
    download_url_to_file(
        url='https://www.ons.gov.uk/datasets/create/filter-outputs/7f980d49-d9ec-48a6-90f3-6373ad81491a?f=get-data&format=csv',
        local_file='unpaid_carer.csv'
    )


if __name__ == "__main__":
    ROOT_DIR = Path(__file__).parent.joinpath(
        '../../data/raw/neet-factors').resolve()
    ROOT_DIR.mkdir(parents=True, exist_ok=True)
    os.chdir(ROOT_DIR)

    main()
