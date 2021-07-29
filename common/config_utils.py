# --coding:utf-8--
import os
import configparser

current = os.path.dirname(__file__)
config_path = os.path.join(current,'../conf/config.ini')

class ConfigUtils:
    def __init__(self,config_path=config_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_path,encoding='utf-8')

    def get_url(self):
        value = self.config.get('default','url')
        return value


config = ConfigUtils()
if __name__=='__main__':
    print(config.get_url())
