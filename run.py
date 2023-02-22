from src.api_elexon_caller import ElexonCaller
from src.helper import adding_minutes_to_df
from src.metrics import Report
import datetime as dt

if __name__ == '__main__':

    today = dt.datetime.today()
    yesterday = today - dt.timedelta(days=1)

    ec = ElexonCaller(settlement_date=yesterday.strftime('%Y-%m-%d'))

    daily_imbalanced_prices = ec.get_daily_imbalanced_prices()
    daily_aggregated_imbalanced_volumes = ec.get_daily_aggregated_imablance_volumes()

    adding_minutes_to_df(daily_imbalanced_prices)
    adding_minutes_to_df(daily_aggregated_imbalanced_volumes)

    daily_report = Report(daily_imbalanced_prices, daily_aggregated_imbalanced_volumes)
    daily_report.print_simple_description()
    daily_report.print_simple_statistics()
    daily_report.plot_graphs()

