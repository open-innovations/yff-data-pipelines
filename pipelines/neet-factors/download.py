import os
import requests


def download_url_to_file(url, local_file):
    r = requests.get(url)
    with open(local_file, 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":
    ROOT_DIR=os.path.realpath(os.path.join(os.path.dirname(__file__), '../../data/raw/neet-factors'))
    os.makedirs(ROOT_DIR, exist_ok=True)
    os.chdir(ROOT_DIR)

    # https://www.gov.uk/government/statistics/children-in-low-income-families-local-area-statistics-2014-to-2022
    clif_url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1145380/children-in-low-income-families-local-area-statistics-2014-to-2022.ods'
    download_url_to_file(
      url=clif_url,
      local_file=os.path.basename(clif_url)
    )
