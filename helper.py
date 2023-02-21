import pandas as pd

float_cols = ['imbalancePriceAmountGBP', 'imbalanceQuantityMAW']
int_cols = ['settlementPeriod']
dt_cols = ['settlementDate']


def convert_dtypes(func):
    """This wrapper attempts to convert common columns to the correct dtype."""

    def inner(*args):

        df = func(*args)
        for col in float_cols:
            try:
                df[col] = df[col].astype(float)
            except KeyError:
                pass

        for col in int_cols:
            try:
                df[col] = df[col].astype(int)
            except KeyError:
                pass

        for col in dt_cols:
            try:
                df[col] = pd.to_datetime(df[col])
            except KeyError:
                pass

        return df
    return inner


def make_it_daily(func):
    """from 1 to 48 periods"""

    def inner(*args):

        dfs = []
        for period in range(1, 49):
            df = func(*args, period)
            df.reset_index(drop=True, inplace=True)
            dfs.append(df)
        master = pd.concat(dfs)
        master.reset_index(drop=True, inplace=True)

        return master
    return inner


def adding_minutes_to_df(df: pd.DataFrame):

    print(0)

