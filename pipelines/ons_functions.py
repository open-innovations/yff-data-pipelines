import pandas as pd


def read_headers(filename, header_rows=7):
    return pd.read_csv(filename, header=None, nrows=header_rows, index_col=0).T.set_index('CDID')


def infer_date(raw_date: pd.Series):
    '''
    Process the date - this is a mixture of Yearly (`YYYY`),
    Quarterly (`YYYY Qx`) and Monthly (`YYYY MMM`), based on
    the date format. Parse these, coercing errors into a valid
    null date (NaT). Store the type of date detected based on
    non-null values. Finally collapse these with a `ffill` to
    construct the `date` column.
    '''
    # Create a blank series the same length as the raw index
    freq = pd.Series(index=raw_date.index, dtype=str)

    # Try to parse a standalone year, coerce any errors to NaT
    year = pd.to_datetime(raw_date, format="%Y", errors="coerce")
    # Set the according vales in freq to 'a' for annual
    freq.loc[year.notna()] = 'a'

    # Try to parse a quarterly measure, coercing errors.
    # There is no built in parser for this, so we need to create our own, by first splitting
    quarter = raw_date.str.split(r'\sQ')
    # If the quarter doesn't contain two values, set the result to NaT
    quarter.loc[quarter.str.len() != 2] = pd.NaT
    # For those that remain, create a date that represents the quarter (Jan = Q1, Apr = Q2, etc)
    # Then parse it
    quarter.loc[quarter.notna()] = quarter.loc[quarter.notna()].map(
        lambda x: f"{x[0]}-{int(x[1])*3 -2}").pipe(pd.to_datetime)
    # Set the freq marker
    freq.loc[quarter.notna()] = 'q'

    # Construct a month series
    month = pd.to_datetime(raw_date, format="%Y %b", errors="coerce")
    # Set the month frequency marker
    freq.loc[month.notna()] = 'm'

    # Check that we don't have any missing dates
    try:
        assert freq.isna().sum() == 0, "Couldn't parse all dates"
    except Exception as e:
        print(str(e))
        print(raw_date[freq.isna()].to_frame())
        raise e

    # Construct a dataframe with all columns, and ffill into the date column,
    # before dropping the year, quarter and month series
    date = pd.DataFrame({
        'year': year,
        'quarter': quarter,
        'month': month,
        'date': None,
        'freq': freq,
    }).ffill(axis=1).drop(columns=['year', 'quarter', 'month'])

    return date
