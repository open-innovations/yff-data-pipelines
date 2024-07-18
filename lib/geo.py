import requests
import io
import geopandas as gpd


def load_geo_data_frame(url):
    '''Load a url to a geopandas dataframe and return it'''
    r = requests.get(url)
    with io.StringIO(r.text) as i:
        data = gpd.GeoDataFrame.from_file(i)
    return data
