import unittest
import os
import sys

# Ajouter le chemin du module au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/shippingboapy_tryno')))

from addresses import Addresses

class TestAddresses(unittest.TestCase):
    def setUp(self):
        self.api_key = 'asRrIM5Q7BBCwcq8Z90Xdb4A5ajM8wJhxwLPgVJ0xpg'
        self.addresses = Addresses(self.api_key)

    def test_get_addresses(self):
        self.assertIsNotNone(self.addresses.get_addresses())
    
if __name__ == '__main__':
    unittest.main(verbosity=2)