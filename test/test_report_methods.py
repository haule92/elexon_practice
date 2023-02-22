import pandas as pd
from src.metrics import Report


def create_test_imbalance_price_data():
    """Creation of dummy data to test the correctness of the methods from the report class.
    The method returns a dataframe simulating the imbalance prices data"""

    col1 = ['Insufficient balance', 'Excess balance', 'Excess balance', 'Insufficient balance', 'Excess balance']
    col2 = [34.65, 761.23, 86.12, 12.98, 78.3333]
    data = {'priceCategory': col1, 'imbalancePriceAmountGBP': col2}
    df = pd.DataFrame(data=data)
    return df


def create_test_aggregated_volume_data():
    """Creation of dummy data to test the correctness of the methods from the report class.
    The method returns a dataframe simulating the aggregated volume data"""

    col1 = ['col1', 'col1', 'col1', 'col1', 'col1']
    col2 = [932.12, 617.58, 905.54, 176.8, 381.9999]
    data = {'col1': col1, 'imbalanceQuantityMAW': col2}
    df = pd.DataFrame(data=data)
    return df


def test_compute_total_imbalance_cost():
    imbalance_price = create_test_imbalance_price_data()
    aggregated_volume = create_test_aggregated_volume_data()

    result = Report(imbalance_price, aggregated_volume).compute_total_imbalance_cost()

    assert result[0] == '47.63'
    assert result[1] == '925.68'


def test_compute_highest_absolut_prices():
    imbalance_price = create_test_imbalance_price_data()
    aggregated_volume = create_test_aggregated_volume_data()

    result = Report(imbalance_price, aggregated_volume).compute_highest_absolut_prices()

    assert result[0] == '34.65'
    assert result[1] == '761.23'


def test_compute_total_imbalance_quantity():
    imbalance_price = create_test_imbalance_price_data()
    aggregated_volume = create_test_aggregated_volume_data()

    result = Report(imbalance_price, aggregated_volume).compute_total_imbalance_quantity()

    assert result == '3,014.04'


def test_compute_highest_absolut_volume():
    imbalance_price = create_test_imbalance_price_data()
    aggregated_volume = create_test_aggregated_volume_data()

    result = Report(imbalance_price, aggregated_volume).compute_highest_absolut_volume()

    assert result == '932.12'


def test_statistics():
    imbalance_price = create_test_imbalance_price_data()
    aggregated_volume = create_test_aggregated_volume_data()
    result = Report(imbalance_price, aggregated_volume).compute_basic_statistics_aggregated_volumne()
    assert type(result) is dict
