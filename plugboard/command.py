# encoding:utf-8

import logging
import os
import pkgutil

from functools import lru_cache
from importlib import import_module
from .commands.cli import BaseCli
from .exceptions import CommandHandlerError

logger = logging.getLogger(__name__)


def find_command_modules():
    """
    find the commands dir modules
    the commands module should in the `commands` directory
    :return:
    """
    # packages default commands
    command_dir = os.path.join(os.path.dirname(__file__), "commands")
    return [name for _, name, is_pkg in pkgutil.iter_modules([command_dir]) if not is_pkg]


def load_commands(name: str):
    """
    load command modules from commands dir
    :return: command instance
    """
    parent_module = __name__.rpartition(".")[0]

    py_module = import_module(".commands.%s" % name, package=parent_module)

    if hasattr(py_module, "Command"):
        return py_module.Command
    else:
        raise CommandHandlerError("subcommand class name must be `Command`")


@lru_cache(maxsize=None)
def get_commands() -> dict:
    """
    get commands
    :return: dict, {command_cls_name:command_cls}
    """
    commands = {}
    modules = find_command_modules()

    for py_module in modules:

        cls = load_commands(py_module)
        if issubclass(cls, BaseCli):
            commands.update({cls.name: cls})
        else:
            raise CommandHandlerError("%s class must implement name in subclass" % cls)
    return commands


class ManagementUtility(object):
    """
    command management utility
    """

    def __init__(self, argv: str):

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

    def fetch_commands(self):
        pass

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
