import unittest

from app import Application
from app.config import UMaxValueOutOfRange, TTaskValueOutOfRange
from tests.test_base import TestConfigBase


class TestSuccess(TestConfigBase):
    """

    """
    file_input = 'example_success_2'
    default_file = f'tests/inputs/{file_input}'
    output_file = f'tests/outputs/{file_input}'
    default_user_entry = [8, 20, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 10, 2]
    ttask_test = 10
    umax_test = 3

    def test_params(self):
        self.assertEqual(self.config_settings.ttask, self.ttask_test, "ttask value isn't the expected")
        self.assertEqual(self.config_settings.umax, self.umax_test, "umax  values isn't the expected")

    def test_user_queue(self):
        self.assertEqual(type(self.default_user_entry), list, "The var default_user_entry isn't list type.")
        self.assertEqual(len(self.config_settings.next_ticks), len(self.default_user_entry),
                         "Queue length isn't the same.")
        for user in self.default_user_entry:
            self.assertEqual(self.config_settings.get_next_tick_users(), user,
                             "The expected users value for this tick is incorrect")

    def test_app_run(self):
        self.assertEqual(self.expected_output, Application(test=True).run())


class TestNoUsers(TestConfigBase):
    """

    """
    file_input = 'test_no_users'

    def test_empty_user_queue(self):
        self.assertEqual(self.expected_output, Application(test=True).run())


class TestTTaskFailure(TestConfigBase):
    """

    """
    file_input = 'test_ttask_error'

    def setUp(self):
        try:
            TestConfigBase.setUp(self)
        except TTaskValueOutOfRange:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "The config didn't raise the correct exception")

    def test_empty_user_queue(self):
        self.assertEqual(self.expected_output, Application(test=True).run())


class TestUMaxFailure(TestConfigBase):
    """

    """
    file_input = 'test_umax_error'

    def setUp(self):
        try:
            TestConfigBase.setUp(self)
        except UMaxValueOutOfRange:
            self.assertTrue(True)
        except:
            self.assertTrue(False, "The config didn't raise the correct exception")

    def test_empty_user_queue(self):
        self.assertEqual(self.expected_output, Application(test=True).run())


if __name__ == '__main__':
    unittest.main()
