import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Bloody Mary", 5.50)
        self.customer = Customer("Noah Clark", 35.00)

    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    # def test_pub_has_cash(self):
    #     self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_drinks_list_length(self):
        self.pub.add_drink(self.drink)
        self.pub.stock_count()
        self.assertEqual(1, self.pub.stock_count())

    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer(self.drink, self.customer)
        self.assertEqual(105.50, self.pub.till)
        self.assertEqual(29.50, self.customer.wallet)