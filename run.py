from src.api_elexon_caller import ElexonCaller
from src.helper import adding_minutes_to_df
from src.plotter import Plotter
from src.metrics import Report


if __name__ == '__main__':

    eep = ElexonCaller(settlement_date='2015-03-01')

    daily_imbalanced_prices = eep.get_daily_imbalanced_prices()
    daily_aggregated_imbalanced_volumes = eep.get_daily_aggregated_imablance_volumes()

    adding_minutes_to_df(daily_imbalanced_prices)
    adding_minutes_to_df(daily_aggregated_imbalanced_volumes)

    Report(daily_imbalanced_prices, daily_aggregated_imbalanced_volumes)

    plotter = Plotter()
    plotter.plot_imbalance_prices(daily_imbalanced_prices)
    plotter.plot_imbalance_quantity(daily_aggregated_imbalanced_volumes)

