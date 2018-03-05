# encoding:utf-8


class GlobalSettings(object):
    REDIS_URL = "redis://@localhost:6379/0"
    DEBUG = True

    TIMEOUT = 10  # 10 seconds

    LOGGERS = {
        "version": 1,
        "formatters": {
            "verbose": {
                "class": "logging.Formatter",
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            },
            "simple": {
                "class": "logging.Formatter",
                "format": "%(levelname)s %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO"
            }
        },
        "root": {
            "level": "DEBUG",
            "handle": ["console"]
        }
    }  # LOGGING CONFIG

    TIMEZONE = "UTC"  # default timezone is in UTC

    RETRY_TIMES = 5  # when exec failure

    COMMANDS = []  # command module dirs

    PLUGINS = []  # plugin module dirs
