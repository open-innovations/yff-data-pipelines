import pandas as pd


def read_metadata_from_excel_sheet(filename, sheet):
    metadata = pd.read_excel(filename, sheet_name=sheet,
                             header=None, skiprows=1, nrows=1)
    metadata = pd.Series(metadata.values.flatten())
    metadata = metadata.dropna()
    metadata = metadata.reset_index(drop=True)
    metadata = pd.DataFrame(
        metadata.iloc[1::2].values, index=metadata.iloc[0::2].str.strip(':')).T
    metadata = metadata.rename(
        columns={
            'Date of publication': 'Release Date',
            'Date of next publication': 'Next release'
        }
    )
    return metadata


def read_headers_from_excel_sheet(filename, sheet):
    headers = pd.read_excel(filename, sheet_name=sheet,
                            index_col=0, header=None, skiprows=4, nrows=3).T
    headers.index.name = 'column'
    headers.columns = pd.Index([
        'age',
        'm1',
        'm2'
    ])
    headers.loc[:, 'age'] = headers.loc[:, 'age'].ffill()
    headers.loc[:, 'm1'] = headers.loc[:, 'm1'].ffill()
    headers.loc[:, 'm2'] = headers.loc[:, 'm2'].fillna('')
    headers = headers.reset_index()
    headers['measure'] = headers.loc[:, ['m1', 'm2']].astype(
        'str').apply('_'.join, axis=1).str.strip('_')
    headers = headers.drop(columns=['m1', 'm2'])
    headers['sheet'] = sheet
    metadata = read_metadata_from_excel_sheet(filename, sheet)
    headers.loc[:, metadata.columns] = metadata.iloc[0].values
    headers = headers.set_index(['sheet', 'column'])
    return headers


def read_data_from_excel_sheet(filename, sheet):
    data = pd.read_excel(filename, sheet, index_col=0,
                         header=None, skiprows=9, na_values=['..', '*'])

    # Get rid of trailing rows
    data = data[data.iloc[:, 0].notna()]
    data = data.astype(float)

    data.index.name = 'date'

    # Every 5th column is a rate
    non_rate_columns = data.columns[[
        (x + 1) % 5 != 0 for x in range(data.columns.size)]]
    # Round the non-rate columns
    data.loc[:, non_rate_columns] = data.loc[:,
                                             non_rate_columns].div(1000).round()

    data = data.melt(var_name='column', ignore_index=False)
    data['sheet'] = sheet

    data = data.reset_index(drop=False).set_index(['sheet', 'column'])
    return data
