# encoding:utf-8
import io
import logging
import unittest.mock

from pluginboard.utils import log


class LoggerTest(unittest.TestCase):
    """
    """
    def setUp(self):
        log.configure_logging()
        self.logger = logging.getLogger("plugboard")
        self.logger_output = io.StringIO()

        self.old_stream = self.logger.handlers[0].stream
        self.logger.handlers[0].stream = self.logger_output

    def tearDown(self):
        self.logger.handlers[0].stream = self.old_stream

    def test_setup_log_config(self):
        """
        :return:
        """
        self.logger.error("error")
        self.assertIn("error", self.logger_output.getvalue())

    # @unittest.mock.patch()
    def test_setup_user_logging(self):
        """
        :return:
        """
