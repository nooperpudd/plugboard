# encoding:utf-8
import traceback


class SettingsImportError(Exception):
    """
    """
    pass


# parameter error
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

# command error


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


class PluginValidationError(Exception):
    """
    plugin failed validation.
    """
    def __init__(self, plugin, message):
        """
        :param plugin: the plugin which failed validation, may be a module or an arbitrary object.
        :param message:
        """
        self.plugin = plugin
        super(Exception, self).__init__(message)

    def __str__(self):
        return "{0.plugin}-{0.message}".format(self)


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





class HookInstanceDead(Exception):
    """The instance bound to a Hook is dead.
    As Panglers only maintain weak references to their instances when bound,
    the instance can be collected before the Pangler. Trying to trigger an
    event in this case raises an InstanceDead exception.
    """
    pass


class TracebackReport(object):
    """
    """

    def trace(self):
        pass
