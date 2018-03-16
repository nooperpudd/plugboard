# encoding:utf-8
import contextlib
import functools
import inspect
import logging
import threading

import io

log = logging.getLogger("plugboard.plugins")


class MetaPlugin(type):
    """
    """
    def __new__(mcs, *args, **kwargs):
        pass

class PluginOutput(io.TextIOWrapper):
    pass


class PluginBase(object):
    """
    """
    def __init__(self, plugin_args=None, *args, **kwargs):
        if plugin_args:
            self.args = plugin_args
        else:
            self.args = {}
        self.callback = None
        self.config = None

    def run(self, *args, **kwargs):
        """
        the core plugin member that should be implemented by
        all plugins.
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    def exception(self):
        """
        :return:
        """
        raise NotImplementedError()

    def failure(self):
        raise NotImplementedError()

    def exit(self):
        raise NotImplementedError()

    def log(self):
        pass




class PluginCore(object):
    """
    """

    def __init__(self):
        self.modules = []
        self.lock = threading.Lock() # lock

    def __call__(self, *args, **kwargs):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def register(self, plugin_cls, **options):

        plugin_modules = []

        if isinstance(plugin_cls, PluginApp):
            plugin_modules.append(plugin_cls)

        for _module in plugin_modules:

            # Ignore the registration if the model has been
            # swapped out.
            # If we got **options then dynamically construct a subclass of
            # admin_class with those **options.
            if options:
                # For reasons I don't quite understand, without a __module__
                # the created class appears to "live" in the wrong place,
                # which causes issues later on.
                options['__module__'] = __name__
                admin_class = type("%s_plugin" % _module.__name__, (plugin_cls,), options)
            else:
                admin_class = type("%s_plugin" % _module.__name__, ())

                # Instantiate the admin class to save in the registry
            self.modules[_module] = admin_class(_module, self)

    def import_modules(self):
        pass

    def get_modules(self):
        pass

    def signal(self):
        pass

    def ready(self):
        pass

    def exception(self):
        pass


def exec_order():
    """
    :return:
    """

    def func(*args, **kwargs):
        @functools.wraps
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    return func


class PluginApp(object):
    """
    """
    def __init__(self, name, priority, timeout, retry_times, lock, **options):
        """
        :param name: plugin name
        :param priority:  plugin priority
        :param timeout:  plugin exec timeout
        :param retry_times: plugin retry times
        :param lock: plugin is locked
        :param options:
        """
        self.name = name
        self.priority = priority
        self.options = options
        self.timeout = timeout
        self.retry_times = retry_times
        self.lock = lock

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, *args, **kwargs):
        pass


    @contextlib.contextmanager
    def locked(self, name):
        """
        :return:
        """
        lock = redis_connect.lock(name)
        have_lock = lock.acquire(blocking=True)
        if have_lock and redis_connect.get(lock_key):
            lock.release()
        return ret_value

    def before_start(self):
        pass

    def failure(self):
        pass

    def start(self):
        pass

    def finished(self):
        pass

    def signal(self):
        pass


class PluginManagement(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.plugins = []

    def register(self, module_or_iterable, **options):
        """
        :param module_or_iterable:
        :return:
        """
        if issubclass(module_or_iterable, PluginBase):
            model_or_iterable = [module_or_iterable]

        for _module in module_or_iterable:

            if _module not in self.plugins:
                # If we got **options then dynamically construct a subclass of
                # admin_class with those **options.
                if options:
                    # For reasons I don't quite understand, without a __module__
                    # the created class appears to "live" in the wrong place,
                    # which causes issues later on.
                    options['__module__'] = __name__
                    plugin_class = type("%sPlugin" % _module.__name__, (PluginBase,), options)
                else:
                    plugin_class = _module(self)
                # Instantiate the admin class to save in the registry
                self.plugins[_module] = plugin_class

    def start(self, *args, **kwargs):

        for plugin_app in self.plugins:
            name = plugin_app.name
            is_lock = plugin_app.is_lock
            lock_arg = plugin_app.lock_arg
            timeout = plugin_app.timeout
            call_args = inspect.getcallargs(**kwargs)

            if is_lock:

                lock_key = call_args.get(lock_arg)
                lock_key = "plugin-" + str(lock_key)
                lock = redis_connect.lock(lock_key, timeout=timeout)
                have_lock = lock.acquire(blocking=True)
                if have_lock:
                    results = self._plugin_start(name,plugin_app,*args,**kwargs)

    def _plugin_start(self, name, app, *args, **kwargs):
        try:
            results = app.start(*args, **kwargs)
        except Exception as e:
            self.failure(name, *args, e)
        else:
            return results

    def failure(self, name, args, ex):
        log.exception("exception occurred:", name, args, ex)


plugin_core = PluginCore()


class PluginUtility(object):

    def __init__(self):
        pass
    def load_plugins(self):
        pass
