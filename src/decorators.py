import pandas as pd
from tqdm import tqdm
from src.helper import float_cols, int_cols, dt_cols


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
        for period in tqdm(range(1, 49)):
            df = func(*args, period)
            df.reset_index(drop=True, inplace=True)
            dfs.append(df)
        master = pd.concat(dfs)
        master.reset_index(drop=True, inplace=True)

        return master
    return inner


def format_readable(func):

    def inner(*args):
        number = func(*args)
        if type(number) is list:
            return "{:,}".format(round(number[0], 2)), "{:,}".format(round(number[1], 2))
        return "{:,}".format(round(number, 2))
    return inner

