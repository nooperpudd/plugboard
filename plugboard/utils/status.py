# encoding:utf-8

from enum import Enum, auto


class TaskEvent(Enum):
    PENDING = auto()
    RUNNING = auto()
    KILLED = auto()
    FAILURE = auto()
    SUCCESS = auto()
    UNKNOWN = auto()


TASK_RUNNING_TIME = ""
TASK_RETRY_TIMES = ""

# task timeout , retry times
# task killed, or task
