import configparser
from pathlib import Path


class Credentials:
    """Credentials class to read the credentials for different of accounts, emails, apis or databases.
    This information is usually stored locally and gitignored in the repo under the name 'config.ini'.
    The parents of the ROOT DIR depends on where the class Credentials is defined."""

    ROOT_DIR = Path(__file__).parents[1]
    CONFIG_FILENAME = ROOT_DIR.joinpath('config.ini')

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILENAME)

    def get_elexon_api_key(self):
        definition = 'ELEXON_CREDENTIALS'
        credential_dict = {
            'api_key': self.config[definition]['api_key']
        }
        setattr(self, definition, credential_dict)
