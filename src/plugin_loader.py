import os
import sys

class PluginLoader:
    """Plugin Loader

    Loads the plugins from the `folder` folder.
    """
    plugins = {}

    def __init__(self, folder):
        """Load all available plugins stored in folder"""
        folder = os.path.abspath(folder)

        if not os.path.isdir(folder):
            assert False, "Unable to load plugins because '%s' is not a folder" % folder
            return

        # Append the folder because we need straight access
        sys.path.append(folder)
        # Build list of folders in directory
        to_import = [f for f in os.listdir(folder) if not f.endswith(".pyc")]

        for module in to_import:
            self.__load_em(module)

    def __load_em(self, module):
        """Attempt to load the plugin"""
        if module.endswith(".py"):
            name = module [:-3]
        else:
            name = module

        try:
            __import__(name)
        except ImportError, e:
            print "Import error for: %s" % name
            return

        plugin = sys.modules[name]

        assert hasattr(plugin, "info"), "You have to have `info` dict within you plugin. Check hello_world example."

        if hasattr(plugin, plugin.info["main"]):
            self.plugins[plugin.info["name"]] = plugin

    def init_plugins(self, *args, **kwargs):
        for p in self.plugins:
            self.init_plugin(p, *args, **kwargs)

    def init_plugin(self, name, *args, **kwargs):
        """Creates a new instance of a plugin `name`

        any other parameters passed will be sent to the __init__ function
        of the plugin, including those passed by keyword
        """
        plugin = self.plugins[name]
        return getattr(plugin, plugin.info["main"])(*args, **kwargs)
