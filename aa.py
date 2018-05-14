# encoding:utf-8

class Manger(object):
    def __init__(self,name=None):
        self.name = name

    def plugin(self,*args,**kwargs):
        def _create_plugin_cls(**options):
            def _create_plugin(func):
                pass

                return _create_plugin
            # return _create_plugin_cls

        return _create_plugin_cls(**kwargs)
