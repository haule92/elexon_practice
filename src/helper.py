import pandas as pd
import datetime as dt

float_cols = ['imbalancePriceAmountGBP', 'imbalanceQuantityMAW']
int_cols = ['settlementPeriod']
dt_cols = ['settlementDate']


def adding_minutes_to_df(df: pd.DataFrame):
    df['settlementDate'] = df.apply(lambda x: x['settlementDate'] + dt.timedelta(minutes=30 * x['settlementPeriod']),
                                     axis=1)
