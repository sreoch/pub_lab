import unittest
from src.food import Food


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Nachos", 5.00, 2)
        self.food_2 = Food("Pizza", 8, 4)

    
