import unittest
import os
import sys

# Ajouter le chemin du module au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/shippingboapy_tryno')))

from addresses import Addresses

class TestAddresses(unittest.TestCase):
    def setUp(self):
        
        self.addresses = Addresses()

    def test_get_addresses(self):
        self.assertIsNotNone(self.addresses.get_addresses())
    
if __name__ == '__main__':
    unittest.main(verbosity=2)