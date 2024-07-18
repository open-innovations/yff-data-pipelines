from pathlib import Path
from lib.downloader import download_url_to_file
from lib.util import set_working_directory
from lib.geo import load_geo_data_frame

ROOT = (Path(__file__).parent / '../..').resolve()


with set_working_directory(ROOT / 'data/reference/'):
    download_url_to_file(
        "https://cdn.jsdelivr.net/gh/odileeds/hexmaps/maps/uk-constituencies-2023.hexjson")

    # Search page:
    # https://geoportal.statistics.gov.uk/search?categories=%252Fcategories%252Fboundaries%2520-%2520electoral%252F2024&q=Future_Parlicons&sort=Title%7Ctitle%7Casc&tags=Boundaries
    # or:
    # https://geoportal.statistics.gov.uk/datasets/ons::westminster-parliamentary-constituencies-july-2024-boundaries-uk-bgc-2/about
    # Parliamentary constituencies:
    #   BGC = Generalised to 20m and clipped to coastline
    #   BSC = Super-generalised (200m) clipped to coastline
    #   BUC = Ultra-generalised (500m) clipped to coastline
    # From that page, select "I want to use this" at the bottom then View API Resources, and Open in API Explorer
    # Change options, and copy the query string - alter the f=json to f=geojson
    geo="Westminster_Parliamentary_Constituencies_July_2024_Boundaries_UK_BSC"
    pcon_url = f"https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/{geo}/FeatureServer/0/query?where=1%3D1&outFields=PCON24CD,PCON24NM,PCON24NMW&outSR=4326&f=geojson"
    pcon = load_geo_data_frame(pcon_url)
    # NB Rounded to 5 decimal places
    pcon.to_file('uk-constituencies-2024.geojson', coordinate_precision=5)
