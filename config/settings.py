import logging
import logging.config
import yaml

'''
    Login setup
'''
with open('../config/logger_config.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

logging.config.dictConfig(config)