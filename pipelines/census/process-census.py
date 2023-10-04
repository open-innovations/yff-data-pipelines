import os
import pandas as pd

OUT_PATH = os.path.join('../..', 'data', 'processed', 'census')

if __name__ == '__main__':
    data = pd.read_csv(
        '../../data/raw/census.csv'
    )

    data.columns = data.columns.str.lower()
    data = data.rename(
        columns={
        'obs_value': 'value',
        'obs_status_name': 'notes',
        'c2021_nssec_10_name': 'variable_name'
        }
    )

    data.variable_name = data.variable_name.str.strip()

    data['rate'] = (data.value / 
                    (data.groupby('geography_code')['value'].transform('first')) * 100)

    data.to_csv(os.path.join(OUT_PATH, 'unemployed_never_worked.csv'), index=False)





    