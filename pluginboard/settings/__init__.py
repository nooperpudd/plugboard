# encoding:utf-8
import copy
import importlib

from pluginboard.exceptions import SettingsImportError
from .global_settings import GlobalSettings


class ConfigSettings(dict):
    """
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()

    def setup(self, defaults=GlobalSettings):
        """
        load settings form default global
        :return:
        """
        self.from_object(defaults)

    def import_string(self, path, silent):
        """
        :param path:
        :param silent:
        :return:
        """
        import_name = path.replace(":", ".")
        module_path, cls_obj = import_name.rsplit(".", 1)
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, cls_obj):
                return getattr(module, cls_obj)
            else:
                if not silent:
                    raise SettingsImportError("import <%s>.<%s> class does not exist" % (module_path, cls_obj))

        except (ImportError, AttributeError):
            if not silent:
                raise SettingsImportError("<%s>Settings Import Error" % path)

    def from_object(self, obj, silent=True):
        """
        # local settings from pyobject
        if obj -> str,
         from_object("app.config")
        :param obj:
        :param silent:
        :return:
        """
        if isinstance(obj, str):
            obj = self.import_string(obj, silent)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)

    def __getattr__(self, item):
        return self[item]

    def __deepcopy__(self, memo):
        return ConfigSettings(copy.deepcopy(dict(self)))

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))


config = ConfigSettings()
