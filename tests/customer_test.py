import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Noah Clark", 35.00, 27)
        self.customer_2 = Customer("Scott Reoch", 10.00, 15)

    def test_customer_has_name(self):
        self.assertEqual("Noah Clark", self.customer.name)

    def test_customer_has_age(self):
        self.assertEqual(27, self.customer.age)

    def test_wallet_decrease(self):
        self.customer.wallet_decrease(2.50)
        self.assertEqual(32.50, self.customer.wallet)

    def test_customer_drunkness_drink(self):
        drink = Drink("Bloody Mary", 5.50, 2)
        self.customer.increase_drunkness_level(drink)
        self.assertEqual(2, self.customer.drunkness_level)

    def test_customer_drunkness_food(self):
        food = Food("Pizza", 5.00, 4)
        self.customer.decrease_drunkness_level(food)
        self.assertEqual(-4, self.customer.drunkness_level)
