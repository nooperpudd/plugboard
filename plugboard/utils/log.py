# encoding:utf-8
import logging
import logging.config

from plugboard.settings import config


class RequireDebugFalse(logging.Filter):

    def filter(self, record):
        return not config.DEBUG


class RequireDebugTrue(logging.Filter):
    def filter(self, record):
        return config.DEBUG


DEFAULT_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        'debug_false': {
            '()': 'plugboard.utils.log.RequireDebugFalse',
        },
        'debug_true': {
            '()': 'plugboard.utils.log.RequireDebugTrue',
        },
    },
    "formatters": {
        "details": {
            "class": "logging.Formatter",
            "format": "%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s",
        },
        "default": {
            "class": "logging.Formatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
        },
        "plugins": {
            "class": "",
            "format": ""
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "filters": ["debug_true"],
            "formatter": "default",
        },
        "commands": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "filters": ["debug_true"],
            "formatter": "default"
        },
        "plugins": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "plugins"
        }
    },
    "loggers": {
        "plugboard": {
            "level": "INFO",
            "handlers": ["console"]
        },
        "plugboard.commands": {
            "level": "INFO",
            "handlers": ["commands"],
            "propagate": False
        },
        "plugboard.plugins": {
            "level": "INFO",
            "handlers": ["plugins"],
            "propagate": False
        }

    }
}  # LOGGING CONFIG


def configure_logging(logging_config):
    """
    :param logging_config:
    :return:
    """
    logging.config.dictConfig(DEFAULT_LOGGING)
    if logging_config:
        logging.config.dictConfig(logging_config)
