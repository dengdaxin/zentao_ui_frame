# encoding:utf-8
# @author:ddx
# @time:2021/8/1 10:28
import logging
import os
import time
from common.config_utils import config

now = time.strftime('%Y_%m_%d_%H_%M_%S')
current = os.path.dirname(__file__)
log_path = os.path.join(current,'..' + config.log_path)

class LogUtils(object):
    def __init__(self,logger=None):
        self.log_name = os.path.join(log_path,'%s.log' % now)
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(config.log_level)

        self.fh = logging.FileHandler(self.log_name,'a',encoding='GBK')
        self.fh.setLevel(config.log_level)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(config.log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger

logger = LogUtils().get_log()

if __name__=='__main__':
    logger.info('123')
    logger.error('1')

# class LogUtils():
#     def __init__(self,log_path=config.log_path):
#         self.logfile_path = log_path