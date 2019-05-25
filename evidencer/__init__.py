import os
import glob

class DefaultDirectory:

    package_directory = os.path.abspath(os.path.dirname(__file__))

    @classmethod
    def extractors_plugins(cls):
        return os.path.join(cls.package_directory, "extractors")

    @classmethod
    def extractors_configurations(cls):
        return os.path.join(cls.package_directory, "extractors_configurations")


class Evidencer:
    def __init__(self, extractors_directories=None, extractors_configurations_directories=None):
        self.extractors_plugins_directory = extractors_directories
        self.extractors_configurations_directory = extractors_configurations_directories
        self._extractors = {}
        self._extractors_configurations = {}

    def _import_extractor_configurations(self):
        for directory in self.extractors_configurations_directory:
            for file_configuration in glob.glob(os.path.join(directory, "*.json")):
                self._import_extractor_configuration(file_configuration)

    def _import_extractor_configuration(self, file_configuration):
        pass

    def _import_extractors(self):
        pass

    def extract_by_bindings(self, bindings):
        pass

    def extract(self, extractor_name, extractor_parameters):
        pass

