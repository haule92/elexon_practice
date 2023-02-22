import plotly.express as px


class Plotter:

    @staticmethod
    def plot_imbalance_prices(df):
        date = df.loc[0, 'settlementDate'].strftime('%Y-%m-%d')
        fig = px.line(df,
                      x='settlementDate',
                      y='imbalancePriceAmountGBP',
                      color='priceCategory',
                      title=f'Imbalanced Price Daily Report as of {date}')
        fig.show()

    @staticmethod
    def plot_imbalance_quantity(df):
        date = df.loc[0, 'settlementDate'].strftime('%Y-%m-%d')
        fig = px.line(df,
                      x='settlementDate',
                      y='imbalanceQuantityMAW',
                      color='documentType',
                      title=f'Imbalanced Quantity Daily Report as of {date}')
        fig.show()
