# encoding:utf-8
import logging
import logging.config

from plugboard.settings import config
from plugboard.settings.global_settings import DEFAULT_LOGGING


class RequireDebugFalse(logging.Filter):

    def filter(self, record):
        return not config.DEBUG


class RequireDebugTrue(logging.Filter):
    def filter(self, record):
        return config.DEBUG


def configure_logging(logging_config=None):
    """
    :param logging_config: logging config dict
    :return:
    """
    logging.config.dictConfig(DEFAULT_LOGGING)
    if logging_config:
        logging.config.dictConfig(logging_config)
