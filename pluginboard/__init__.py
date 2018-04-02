# encoding:utf-8
import coloredlogs

from pluginboard.settings import config
from pluginboard.utils.log import configure_logging

coloredlogs.install(config.LOG_LEVEL)

__version__ = "0.1.0"


def get_version():
    """
    :return:
    """
    return __version__


def setup():
    """
    :return:
    """
    configure_logging(config.LOGGER)
