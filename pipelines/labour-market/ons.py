import pandas as pd
import xlrd


def get_sheet_names(filename):
    return xlrd.open_workbook(filename).sheet_names()

def detect_id_row(filename):
    test = pd.read_excel(filename, sheet_name='People', header=None, usecols=[0])[0]
    return test[test == 'Dataset identifier code'].index.to_list().pop()


def get_headers(filename, sheet_name, id_row):
    headers = pd.read_excel(filename, sheet_name=sheet_name, index_col=0, header=None).head(id_row+1).T.set_index('Dataset identifier code').ffill()
    headers = headers.loc[:, headers.columns.isna()]
    headers.columns = ['age', 'measure', 'measure_type']
    headers.measure = headers.measure.str.replace(r'\s+', ' ', regex=True)
    return headers


def add_group(data, value):
    data['group'] = value
    return data


def load_data(filename, sheet_name, id_row):
    data = pd.read_excel(filename, sheet_name=sheet_name, skiprows=id_row, na_values=['*']).rename(columns={ 'Dataset identifier code': 'date_name' })
    data = data[data.iloc[:, 1].notna()]
    return data


def create_date_column(data):
    data['date'] = pd.to_datetime(data.date_name.str.slice(4), format="%b %Y") - pd.DateOffset(months=1)
    return data


def melt_table(data):
    return data.melt(id_vars=['date', 'date_name'], var_name='variable_name')