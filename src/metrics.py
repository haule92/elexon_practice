from prettytable import PrettyTable

from src.decorators import format_readable


class Report:

    def __init__(self, imbalance_prices, imbalance_quantity):
        self.imbalance_prices = imbalance_prices
        self.imbalance_quantity = imbalance_quantity
        self.print_report()

    @format_readable
    def compute_total_imbalance_cost(self):
        insufficient_balance = self.imbalance_prices.loc[
            self.imbalance_prices['priceCategory'] == 'Insufficient balance', 'imbalancePriceAmountGBP'].sum()
        excess_balance = self.imbalance_prices.loc[
            self.imbalance_prices['priceCategory'] == 'Excess balance', 'imbalancePriceAmountGBP'].sum()
        return [insufficient_balance, excess_balance]

    @format_readable
    def compute_highest_absolut_prices(self):
        insufficient_balance = self.imbalance_prices.loc[
            self.imbalance_prices['priceCategory'] == 'Insufficient balance', 'imbalancePriceAmountGBP'].max()
        excess_balance = self.imbalance_prices.loc[
            self.imbalance_prices['priceCategory'] == 'Excess balance', 'imbalancePriceAmountGBP'].max()
        return [insufficient_balance, excess_balance]

    @format_readable
    def compute_total_imbalance_quantity(self):
        result = self.imbalance_quantity['imbalanceQuantityMAW'].sum()
        return result

    @format_readable
    def compute_highest_absolut_volume(self):
        result = self.imbalance_quantity['imbalanceQuantityMAW'].max()
        return result

    def print_report(self):
        my_table = PrettyTable(["Description", "Amount", "Unit"])
        my_table.add_row(['Total Insufficient Balance', self.compute_total_imbalance_cost()[0], 'GBP'])
        my_table.add_row(['Total Excess Balance', self.compute_total_imbalance_cost()[1], 'GBP'])
        my_table.add_row(['Highest Absolut Insufficient Balance', self.compute_total_imbalance_cost()[0], 'GBP'])
        my_table.add_row(['Highest Absolut Excess Balance', self.compute_total_imbalance_cost()[1], 'GBP'])
        my_table.add_row(['Total Imbalance Quantity', self.compute_total_imbalance_quantity(), 'MWh'])
        my_table.add_row(['Highest Absolut Quantity', self.compute_highest_absolut_volume(), 'MWh'])
        print(my_table)
