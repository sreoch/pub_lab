import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Bloody Mary", 5.50, 2)
        self.drink_2 = Drink("Long Island Icetea", 5.50, 10)
        self.customer = Customer("Noah Clark", 35.00, 27)
        self.customer_2 = Customer("Scott Reoch", 10.00, 15)
        self.food_2 = Food("Pizza", 8.00, 4)

    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)



    def test_check_customer_age_okay(self):
        self.assertEqual(True, self.pub.check_customer_age(self.customer))

    def test_check_customer_age_not_okay(self):
        self.assertEqual(False, self.pub.check_customer_age(self.customer_2))

    def test_sell_drink_to_customer_is_over_18(self):
        self.pub.sell_drink_to_customer(self.drink, self.customer)
        self.assertEqual(105.50, self.pub.till)
        self.assertEqual(29.50, self.customer.wallet)

    def test_sell_drink_to_customer_is_under_18(self):
        self.pub.sell_drink_to_customer(self.drink, self.customer_2)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(10.00, self.customer_2.wallet)
    
    def test_sell_drink_to_customer_is_under_limit(self):
        self.pub.sell_drink_to_customer(self.drink_2, self.customer)
        self.assertEqual(105.50, self.pub.till)
        self.assertEqual(29.50, self.customer.wallet)

    def test_sell_drink_to_customer_is_over_limit(self):
        self.customer.increase_drunkness_level(self.drink_2)
        self.pub.sell_drink_to_customer(self.drink_2, self.customer)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(35.00, self.customer.wallet)

    def test_sell_food_to_customer(self):
        self.pub.sell_food_to_customer(self.food_2, self.customer)
        self.assertEqual(108.00, self.pub.till)
        self.assertEqual(27.00, self.customer.wallet)

    def test_stock_value(self):
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink_2)
        self.assertEqual(3, self.pub.stock_value())

