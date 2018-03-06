# encoding:utf-8
import unittest
from plugboard.command import ManagementUtility, execute_command
from plugboard.settings import config
from .user_settings.local import Local
from plugboard.command import find_command_modules

class TestCommands(unittest.TestCase):

    def setUp(self):
        config.from_object(Local)

    def tearDown(self):
        pass
    def test_find_commands(self):
        pass
    def test_load_commands(self):
        pass

    
