# encoding:utf-8
import copy
import unittest

from plugboard.exceptions import SettingsImportError
from plugboard.settings import GlobalSettings
from .user_settings.local import Local, Product


class TestLoadSettings(unittest.TestCase):
    """
    """

    def setUp(self):
        from plugboard.settings import config
        self.config = copy.deepcopy(config)

    def tearDown(self):
        self.config = None

    def test_global_settings(self):
        for key in GlobalSettings.__dict__:
            if key.isupper():
                self.assertEqual(GlobalSettings.__dict__[key], self.config[key])

    def test_load_user_settings(self):
        self.config.from_object(Local)

        for key in Local.__dict__:
            if key.isupper():
                self.assertEqual(Local.__dict__[key], self.config[key])

    def test_load_user_override_settings(self):
        self.config.from_object(Product)

        for key in Product.__dict__:
            if key.isupper():
                self.assertEqual(Product.__dict__[key], self.config[key])

        self.assertNotEqual(Local.COMMANDS, self.config["COMMANDS"])

    def test_load_user_settings_import(self):

        self.config.from_object("tests.user_settings.local.Product")

        for key in Product.__dict__:
            if key.isupper():
                self.assertEqual(Product.__dict__[key], self.config[key])

    def test_silent_failed(self):
        """
        :return:
        """
        with self.assertRaises(SettingsImportError):
            self.config.from_object("test.bbb", silent=False)

    def test_silent_import_error(self):
        """
        :return:
        """
        with self.assertRaises(SettingsImportError):
            self.config.from_object("test.user_settings.local.GlobalData",
                                    silent=False)

    def test_import_error_with_silent(self):
        """
        :return:
        """
        self.config.from_object("test.user_settings.bbb")

        for key in GlobalSettings.__dict__:
            if key.isupper():
                self.assertEqual(GlobalSettings.__dict__[key], self.config[key])
