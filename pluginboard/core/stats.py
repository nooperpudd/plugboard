# encoding:utf-8

import functools
from ..utils import status


def change_state_decorator(func):
    """
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        self.change_state()
        return ret

    return wrapper


class StateEngine(object):
    # skip some staff

    def __init__(self):
        self.state = status.TaskEvent()

    def change_state(self):
        self.state = states[self.state]

    @change_state_decorator
    def func1(self):
        pass

    @change_state_decorator
    def func2(self):
        pass
