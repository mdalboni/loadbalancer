import unittest

from app import config_settings


class TestConfigBase(unittest.TestCase):
    """
    Base class for tests loading default presets
    """
    file_input = 'example_success'

    default_file = f'tests/inputs/{file_input}'
    output_file = f'tests/outputs/{file_input}'

    default_user_entry = [1, 3, 0, 1, 0, 1]
    ttask_test = 4
    umax_test = 2
    expected_output = ''
    config_settings: config_settings = config_settings

    def setUp(self):
        with open(self.output_file, 'r') as f:
            self.expected_output = f.read()
        self.config_settings.setup_config(self.default_file)
