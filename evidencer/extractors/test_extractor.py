from yapsy.IPlugin import IPlugin


class TestExtractor(IPlugin):
    def extract(self, parameters):
        print("Test extractor succefull")


