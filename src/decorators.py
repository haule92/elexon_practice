import pandas as pd
import numpy as np
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
    """The function works as a iterator to concat all the responses of one day.
    From the documentation, each period is 30min, meaning a complete day has 48 periods.
    This can be modified in the case we want fewer periods."""

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
    """Function to format the float numbers to string with thousan comma separator and rounded to two decimal places.
    Since this function is used with data manipulated with pandas, the isinstances are done with np.floats"""

    def inner(*args):
        number = func(*args)
        if type(number) is list:
            to_return = []
            for i in number:
                if isinstance(i, np.floating):
                    to_return.append("{:,}".format(round(i, 2)))
                else:
                    to_return.append(i)
            return to_return

        elif type(number) is dict:
            to_return = {}
            for k, v in number.items():
                if isinstance(v, np.floating):
                    to_return.update({k: "{:,}".format(round(v, 2))})
                else:
                    to_return.update({k: v})
            return to_return

        return "{:,}".format(round(number, 2))
    return inner

