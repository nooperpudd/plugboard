# encoding:utf-8

from enum import Enum, auto


class TaskEvent(Enum):
    PENDING = auto()
    RUNNING = auto()
    FAILURE = auto()
    SUCCESS = auto()
    UNKNOWN = auto()
    KILLED = auto()

class PluginStatus(Enum):
    pass