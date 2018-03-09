# encoding:utf-8

import unittest
import unittest.mock
from plugboard.utils import log


class LoggerTest(unittest.TestCase):
    """
    """
    def test_setup_log_config(self):
        """
        :return:
        """
        log.configure_logging()

    # @unittest.mock.patch()
    def test_setup_user_logging(self):
        """
        :return:
        """
        
