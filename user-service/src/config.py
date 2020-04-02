import logging


class Config(object):
    DB_HOST = 'localhost'
    DB_USERNAME = 'test'
    DB_PASSWORD = 'test@2020'
    DB_NAME = 'test'
    DB_AUTH = 'SCRAM-SHA-256'
    DB_COLLECTION_USERS = 'users'
    DB_COLLECTION_TALKS = 'talks'
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(module)s:%(funcName)s:%(lineno)d — %(message)s'
