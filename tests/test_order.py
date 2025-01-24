import unittest
import os
import sys

# Ajouter le chemin du module au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/shippingboapy_tryno')))

from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order()

    def test_get_order(self):
        order_id = '112842783'
        response = self.order.get_order(order_id)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)  # Assuming the response is a dictionary

    
if __name__ == '__main__':
    unittest.main(verbosity=2)