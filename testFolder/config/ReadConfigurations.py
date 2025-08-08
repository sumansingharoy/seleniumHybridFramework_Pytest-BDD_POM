import configparser
import os

class ReadConfigurations:
    @staticmethod
    def read_configurations(section, key):
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        print(config_path)
        config.read(config_path)

        return config.get(section, key)
