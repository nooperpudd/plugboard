# encoding:utf-8
class GlobalSettings(object):

    REDIS_URL = "redis://@localhost:6379/0"

    DEBUG = True

    LOG_LEVEL = "INFO"

    TIMEOUT = 10  # 10 seconds

    TIMEZONE = "UTC"  # default timezone is in UTC

    RETRY_TIMES = 5  # when exec failure

    COMMANDS = []  # command module dirs

    PLUGINS = []  # plugin module dirs

    LOGGING = {} # consum logging configuration


