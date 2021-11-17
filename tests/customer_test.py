import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Noah Clark", 35.00)
    
    def test_drink_has_name(self):
        self.assertEqual("Noah Clark", self.customer.name)

    def test_increase_till(self):
        self.customer.wallet_decrease(2.50)
        self.assertEqual(32.50, self.customer.wallet)