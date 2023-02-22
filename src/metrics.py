from prettytable import PrettyTable
from collections import Counter
from src.decorators import format_readable
from src.plotter import Plotter


class Report:
    """Class to generate the daily report with simple statistics and plots."""

    def __init__(self, imbalance_prices, imbalance_quantity):
        self.imbalance_prices = imbalance_prices
        self.imbalance_quantity = imbalance_quantity

    @staticmethod
    def wrapper(df, column_to_filter, name_to_filter, column):
        return df.loc[df[column_to_filter] == name_to_filter, column]

    @format_readable
    def compute_total_imbalance_cost(self):
        """Method to compute the total amount of imbalance cost, for each price category."""

        insufficient_balance = self.wrapper(
            self.imbalance_prices, 'priceCategory', 'Insufficient balance', 'imbalancePriceAmountGBP').sum()
        excess_balance = self.wrapper(
            self.imbalance_prices, 'priceCategory', 'Excess balance', 'imbalancePriceAmountGBP').sum()
        return [insufficient_balance, excess_balance]

    @format_readable
    def compute_highest_absolut_prices(self):
        """Method to compute the max absolut prices for both categories in during the day."""

        insufficient_balance = self.imbalance_prices.loc[
            self.imbalance_prices['priceCategory'] == 'Insufficient balance', 'imbalancePriceAmountGBP'].max()
        excess_balance = self.imbalance_prices.loc[
            self.imbalance_prices['priceCategory'] == 'Excess balance', 'imbalancePriceAmountGBP'].max()
        return [insufficient_balance, excess_balance]

    @format_readable
    def compute_total_imbalance_quantity(self):
        """Method to compute the total amount of aggregated quantity."""

        result = self.imbalance_quantity['imbalanceQuantityMAW'].sum()
        return result

    @format_readable
    def compute_highest_absolut_volume(self):
        """Method to compute the max absolut value of quantity."""

        result = self.imbalance_quantity['imbalanceQuantityMAW'].max()
        return result

    @format_readable
    def compute_basic_statistics_imbalance_price(self):
        """Method to compute simple statistics using describe method from pandas"""

        result = {}
        for i in ['Insufficient balance', 'Excess balance']:
            statistics = self.wrapper(self.imbalance_prices, 'priceCategory', i, 'imbalancePriceAmountGBP').describe()
            statistics_dict = dict(statistics)
            c = Counter()
            for k, v in statistics_dict.items():
                c.update({'Imbalance price ' + i + ' ' + k: v})
            result.update(c)
        return result

    @format_readable
    def compute_basic_statistics_aggregated_volumne(self):
        """Method to compute simple statistics using describe method from pandas."""

        result = {}
        statistics = self.imbalance_quantity['imbalanceQuantityMAW'].describe()
        statistics_dict = dict(statistics)
        c = Counter()
        for k, v in statistics_dict.items():
            c.update({'Aggregated volume ' + ' ' + k: v})
        result.update(c)
        return result

    def print_simple_description(self):
        """Method to print the simple descriptions."""

        my_table = PrettyTable(["Description", "Amount", "Unit"])
        my_table.add_row(['Total Insufficient Balance', self.compute_total_imbalance_cost()[0], 'GBP'])
        my_table.add_row(['Total Excess Balance', self.compute_total_imbalance_cost()[1], 'GBP'])
        my_table.add_row(['Total Imbalance Quantity', self.compute_total_imbalance_quantity(), 'MWh'])
        my_table.add_row(['Total Imbalance Quantity', self.compute_highest_absolut_volume(), 'MWh'])
        print(my_table)

    def print_simple_statistics(self):
        """Method to print the simple statics."""

        my_table = PrettyTable(["Simple statistics", "Value"])
        for k, v in self.compute_basic_statistics_imbalance_price().items():
            my_table.add_row([k, v])
        for k, v in self.compute_basic_statistics_aggregated_volumne().items():
            my_table.add_row([k, v])
        print(my_table)

    def plot_graphs(self):
        """Method to plot the timeseries for the two different datasets."""

        plotter = Plotter()
        plotter.plot_imbalance_prices(self.imbalance_prices)
        plotter.plot_imbalance_quantity(self.imbalance_quantity)
