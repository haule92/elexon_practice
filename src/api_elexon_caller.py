import requests
import pandas as pd
from src.decorators import convert_dtypes, make_it_daily
from src.credentials import Credentials


class ElexonCaller(Credentials):

    def __init__(self, settlement_date):
        Credentials.__init__(self)
        self.get_elexon_api_key()
        self.api_key = getattr(self, 'ELEXON_CREDENTIALS')['api_key']
        self.settlement_date = settlement_date

    @staticmethod
    def build_url(report_code, api_key, settlement_date, period):
        return f'https://api.bmreports.com/BMRS/{report_code}/' \
               f'v1?APIKey={api_key}&SettlementDate={settlement_date}&Period={period}&ServiceType=xml'

    def fetch_response(self, report_code, period=1):
        response = requests.get(url=self.build_url(report_code, self.api_key, self.settlement_date, period))
        return response

    @make_it_daily
    def parsed_response(self, report_code, period):
        response = self.fetch_response(report_code, period)
        df = pd.read_xml(response.text, xpath='.//item')
        return df

    @convert_dtypes
    def get_daily_imbalanced_prices(self):
        """B1770"""
        report_code = 'B1770'
        df = self.parsed_response(report_code)
        return df

    @convert_dtypes
    def get_daily_aggregated_imablance_volumes(self):
        """B1780"""
        report_code = 'B1780'
        df = self.parsed_response(report_code)
        return df
