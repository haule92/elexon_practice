import requests
import pandas as pd
from src.decorators import convert_dtypes, make_it_daily
from src.credentials import Credentials


class ElexonCaller(Credentials):
    """
    API caller for Elexon.
    """
    def __init__(self, settlement_date):
        Credentials.__init__(self)
        self.get_elexon_api_key()
        self.api_key = getattr(self, 'ELEXON_CREDENTIALS')['api_key']
        self.settlement_date = settlement_date

    @staticmethod
    def build_url(report_code, api_key, settlement_date, period):
        """Method to build the url to do the request."""
        return f'https://api.bmreports.com/BMRS/{report_code}/' \
               f'v1?APIKey={api_key}&SettlementDate={settlement_date}&Period={period}&ServiceType=xml'

    def fetch_response(self, report_code, period=1):
        """Method to retrieve the response using the builded url."""
        response = requests.get(url=self.build_url(report_code, self.api_key, self.settlement_date, period))
        return response

    @make_it_daily
    def parsed_response(self, report_code, period):
        """Method to parse the response from xml format into dataframe. The decorator above serves the purpose to
        iterate each parsed response in a complete daily response, all in a dataframe."""
        response = self.fetch_response(report_code, period)
        df = pd.read_xml(response.text, xpath='.//item')
        return df

    @convert_dtypes
    def get_daily_imbalanced_prices(self):
        """From the documentation, the report code B1770 is used to get the desired output.
        Then name of the method describes the data."""
        report_code = 'B1770'
        df = self.parsed_response(report_code)
        return df

    @convert_dtypes
    def get_daily_aggregated_imablance_volumes(self):
        """From the documentation, the report code B1780 is used to get the desired output.
        Then name of the method describes the data."""
        report_code = 'B1780'
        df = self.parsed_response(report_code)
        return df
