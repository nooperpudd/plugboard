# encoding:utf-8
import unittest.mock

from plugboard.cmds import app
from plugboard.command import (load_default_commands,
                               import_commands,
                               get_commands)
# from plugboard.settings import config
from .user_settings.local import Local
from plugboard.exceptions import CommandHandlerError


class TestCommands(unittest.TestCase):

    def test_load_default_commands(self):
        default_cmds = load_default_commands()
        result_cmds = {
            "app": app.Command
        }
        self.assertDictEqual(default_cmds, result_cmds)

    @unittest.mock.patch("plugboard.settings.config")
    def test_import_commands_with_settings(self, config):
        config.from_object(Local)
        print(config)
        user_cmds = import_commands()
        print(user_cmds)

    def test_import_commands(self):
        from .user_commands import cac_command, default_command

        commands = [
            "tests.user_commands.cac_command",
            "tests.user_commands.default_command"
        ]
        user_cmds = import_commands(commands)

        results = {
            "jojo": cac_command.Command,
            "test": default_command.Command
        }
        self.assertDictEqual(results, user_cmds)



    def test_get_commands_conflict(self):

        commands = ("tests.user_commands.temp_command",)

        with self.assertRaises(CommandHandlerError):
            get_commands(commands)

    def test_get_commands(self):
        from .user_commands import cac_command, default_command

        commands = ("tests.user_commands.default_command",)
        default_cmds,import_cmds = get_commands(commands)


        self.assertDictEqual(default_cmds,{
            "app":app.Command
        })
        self.assertDictEqual(import_cmds,{
            "test":default_command.Command
        })


    # def test_import_commands_with_module(self):
        # todo support in laters
    #     from .user_commands import cac_command, default_command
    #
    #     commands = ["tests.user_commands"]
    #     user_cmds = import_commands(commands)
    #
    #     results = {
    #         "jojo": cac_command.Command,
    #         "test": default_command.Command
    #     }
    #     self.assertDictEqual(results, user_cmds)
