# encoding:utf-8
import abc
import argparse
import io
import logging
import operator
import os
import pkgutil
from argparse import ArgumentParser
from functools import lru_cache
from importlib import import_module

import plugboard.utils
from plugboard.exceptions import CommandHandlerError
from plugboard.exceptions import HelpParserError, CommandParserError
from plugboard.settings import config

logger = logging.getLogger(__name__)


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


class BaseCommand(metaclass=abc.ABCMeta):
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


def load_command_modules(modules: list, package=None):
    """
    load command module from module name
    :param modules:
    :param package:
    :return:
    """
    commands = {}
    for module in modules:
        py_module = import_module(module, package=package)
        if hasattr(py_module, "Command") and issubclass(py_module.Command, BaseCommand):
            cmd_cls = py_module.Command
            if cmd_cls.name and cmd_cls.name not in commands:
                commands[cmd_cls.name] = cmd_cls
            else:
                raise CommandHandlerError("Must provide command name Or name have been used by other commands")
        else:
            raise CommandHandlerError("Command name must be `Command` and Command must inherit from `BaseCommand`")
    return commands


def load_default_commands():
    """
    :return: commands dict [cls.name] = cls
    """
    parent_module = __name__.rpartition(".")[0]

    local_cmd_dir = os.path.join(os.path.dirname(__file__), "commands")
    modules = []
    for _, name, is_pkg in pkgutil.iter_modules([local_cmd_dir]):
        if not is_pkg:
            modules.append(".commands.%s" % name)

    return load_command_modules(modules, parent_module)


def import_commands(cmd_modules=None):
    """
    :return:
    """
    modules = []
    if cmd_modules:
        modules.extend(cmd_modules)
    if config["COMMANDS"]:
        modules.extend(config["COMMANDS"])

    return load_command_modules(modules)


@lru_cache(maxsize=None)
def get_commands(cmd_modules=None) -> dict:
    """
    get commands
    :return: dict, {command_cls_name:command_cls}
    """
    commands = {}
    default_cmds = load_default_commands()
    default_cmds = sorted(default_cmds, key=operator.itemgetter(0))

    import_cmds = import_commands(cmd_modules)
    import_cmds = sorted(import_cmds, key=operator.itemgetter(0))
    # check common name keys
    common_keys = plugboard.utils.check_dict_common_keys([import_cmds, default_cmds])
    if common_keys:
        raise CommandHandlerError("%s conflict with the default commands" % common_keys)
    else:
        commands.update(default_cmds)
        commands.update(import_cmds)
    return commands


class ManagementUtility(object):
    """
    command management utility
    """

    def __init__(self, argv: str, *args, **kwargs):

        self.command_name = argv.split()[0]
        self.command_argv = argv.split()[1:]  # command argv
        self.commands = get_commands()

    def help(self):
        """
        :return:
        """
        usage = [
            "Type '<command> -h/--help' for help on a specific command"
            "Available commands:"
        ]
        for command in self.commands:
            usage.append("--> %s" % command)
        message = "\n".join(usage)
        return message

    def execute(self):
        """
        :return:
        """
        try:
            sub_command = self.commands[self.command_name]
        except KeyError:
            self.help()
        else:
            instance = sub_command()
            instance.run_from_argv(self.command_argv)


def execute_command(argv=None):
    """
    :param argv:
    """
    utility = ManagementUtility(argv)
    utility.execute()
