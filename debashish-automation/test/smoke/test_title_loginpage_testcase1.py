import unittest

from app.utils import create_driver_instance


class TestTitle_testcase1(unittest.TestCase):

    def setUp(self):
        self.browser=create_driver_instance.get_driver_instance()

    def tearDown(self):
        self.browser.close()


    def test_title_of_webpage_testcase1(self):

        actual_title = self.browser.title
        expected_title = 'eTIMS : Log In'
        assert actual_title == expected_title
