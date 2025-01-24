import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/shippingboapy_tryno')))
from client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.app_id = 447
        self.api_version = 1
        self.client_id = 'Q8TGUF0QDZVPlDZzck9kIjCs6aj7efqWoNAcnyiljKc'
        self.client_secret = 'TalkAlPu47s331DxTo-z1btOiww_2luCQ-6w5oc4lX0'
        self.client = Client(self.app_id, self.api_version, self.client_id, self.client_secret)
    
    def test_run(self):
        self.assertIsNone(self.client.run('fP_lcOYEyDk5GVpR1EnOYmlCzYi3khbV1DsDcjci864'))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)