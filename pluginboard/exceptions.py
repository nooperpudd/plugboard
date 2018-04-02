# encoding:utf-8
import traceback


class ParameterError(Exception):
    """
    Parameter Error Handler
    """
class MissingParameterError(Exception):
    """
    Missing Parameter Error
    """

class ValidatorError(Exception):
    """
    validator command exception handler
    """
    pass


class CommandHandlerError(Exception):
    """
    Command handler Error
    """
    pass

class CommandParserError(Exception):
    """
    Command Parser Error
    """
    pass


class HelpParserError(Exception):
    """
    Help Parser Error
    """
    pass


class PluginException(Exception):
    """
    Plugin handler exception
    """
    pass


class EventException(Exception):
    """
    event Handler exception
    """
    pass


class WorkFlowException(Exception):
    """
    workflow exception
    """
    pass


class SettingsImportError(Exception):
    """
    """
    pass


class TracebackReport(object):
    """
    """

    def trace(self):
        pass
