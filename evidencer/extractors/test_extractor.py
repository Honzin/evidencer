from yapsy.IPlugin import IPlugin
from evidencer import plugin


class TestExtractor(IPlugin, plugin.AbstractExtractor):
    def extract(self, configuration):
        print("Test extractor")
        print(configuration["parameters"]["specific"])
        return configuration["parameters"]["specific"]


