# encoding:utf-8
class GlobalSettings(object):
    DEBUG = True

    LOG_LEVEL = "INFO"

    TIMEZONE = "Asia/Shanghai"  # default timezone is in UTC

    TIMEOUT = 10  # 10 seconds

    RETRY_TIMES = 5  # when exec failure

    COMMANDS = []  # command module dirs

    PLUGINS = []  # plugin module dirs

    LOGGING = {}  # Custom logging configuration

    DEFAULT_LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            'debug_false': {
                '()': 'pluginboard.utils.log.RequireDebugFalse',
            },
            'debug_true': {
                '()': 'pluginboard.utils.log.RequireDebugTrue',
            },
        },
        "formatters": {
            "details": {
                "class": "logging.Formatter",
                "format": "%(asctime)s %(levelname)-8s %(name)-12s:"
                          " %(module)s %(processName)-10s %(thread)d %(message)s",
            },
            "default": {
                "class": "logging.Formatter",
                "format": "%(asctime)s %(name)-12s: %(levelname)-8s  %(message)s"
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
                "formatter": "details"
            }
        },
        "loggers": {
            "pluginboard": {
                "level": "INFO",
                "handlers": ["console"]
            },
            "pluginboard.commands": {
                "level": "INFO",
                "handlers": ["commands"],
                "propagate": False
            },
            "pluginboard.plugins": {
                "level": "INFO",
                "handlers": ["plugins"],
                "propagate": False
            }

        }
    }  # LOGGING CONFIG
