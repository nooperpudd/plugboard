# encoding:utf-8

import abc
import argparse
import io
from argparse import ArgumentParser

from plugboard.exceptions import HelpParserError, CommandParserError


class HelpAction(argparse.Action):
    """
    """
    def __init__(self, option_strings, dest=argparse.SUPPRESS, default=argparse.SUPPRESS, help=None):
        super(HelpAction, self).__init__(option_strings=option_strings, dest=dest, default=default, nargs=0, help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        """
        :param parser:
        :param namespace:
        :param values:
        :param option_string:
        :return:
        """
        output = io.StringIO()
        parser.print_help(output)
        message = output.getvalue()
        raise HelpParserError(message)


class PluginsArgumentParser(ArgumentParser):
    """
    """

    def error(self, message: str):
        """
        :param message:
        :return:
        """
        raise CommandParserError(message)


class BaseCli(metaclass=abc.ABCMeta):
    """
    """
    name = ""
    description = ""

    def __init__(self):
        """
        """
        self.__parser = PluginsArgumentParser(self.name, self.description, add_help=False)
        self.add_arguments(self.__parser)

        self.__parser.add_argument('-h', '--help', action=HelpAction, default=argparse.SUPPRESS,
                                   help='show this help message')

    @abc.abstractmethod
    def add_arguments(self, parser):
        """
        :param parser:
        :return:
        """
        raise NotImplementedError("subclass must implement add arguments func")

    @abc.abstractmethod
    def handler(self, *args, **options):
        """
        sub class should implement this func
        :param args:
        :param options:
        :return:
        """
        raise NotImplementedError("subclass must implement handler func")

    @abc.abstractmethod
    def notify(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    def run_from_argv(self, argv):
        """
        :param argv:
        """
        try:
            options = self.__parser.parse_args(args=argv)
        except CommandParserError as e:
            raise e
        except HelpParserError as e:
            raise e
        except SystemExit:
            print("SystemExit error")
        else:
            cmd_options = vars(options)
            if cmd_options:
                self.execute(**cmd_options)
            else:
                self.__parser.parse_args(["-h"])

    def execute(self, *args, **options):
        """
        execute the command and notify the message
        """
        if "func" in options:
            func = options.pop("func")
            if callable(func):
                func(**options)
        else:
            self.handler(*args, **options)