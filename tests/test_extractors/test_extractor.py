from yapsy.IPlugin import IPlugin
from evidencer import plugin

import glob


class Result:
    def __init__(self):
        self.label = ""
        self.value = ""


class TestExtractor(IPlugin, plugin.AbstractExtractor):
    @plugin.working_directory_context
    @plugin.save_configuration
    def extract(self, configuration):
        result = Result()
        result.label = configuration["parameters"]["label"]
        result.value = self._extract_file_content()
        return result

    def _extract_file_content(self):
        file_path = glob.glob(self.configuration["parameters"]["file"])[0]
        with open(file_path, "r") as f:
            return f.read()

