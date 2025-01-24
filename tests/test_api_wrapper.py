import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/shippingboapy_tryno')))

from api_wrapper import APIWrapper


class TestAPIWrapper(unittest.TestCase):
    def setUp(self):
        self.api = APIWrapper("C353su-OeNKw298ZZfmhHdOzq8KBzbQ5Yd9OXbr57Ic")

    def test_get_access_token(self):
        self.assertIsNotNone(self.api.get_access_token())

    
if __name__ == '__main__':
    unittest.main(verbosity=2)