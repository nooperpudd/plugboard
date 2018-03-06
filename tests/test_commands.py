# encoding:utf-8
import unittest
import copy
from plugboard.command import ManagementUtility, execute_command
from plugboard.settings import config
from .user_settings.local import Local

class TestCommands(unittest.TestCase):

    def setUp(self):
        self.config = copy.deepcopy(config)
        self.config.from_object(Local)

    def tearDown(self):
        pass
    def test_find_commands(self):
        pass
    def test_load_commands(self):
        pass

    
