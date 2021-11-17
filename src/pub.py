class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock = {}

    
    def increase_till(self, amount):
        self.till += amount
    
    def add_drink(self, drink):
        if drink in self.stock:
            self.stock[drink] += 1
        else:
            self.stock[drink] = 1

    def stock_value(self):
        total = self.stock.values()
        total_stock = sum(total)
        return total_stock

    def sell_drink_to_customer(self, drink, customer):
        if self.check_customer_age(customer) and self.check_customer_drunkness(customer):
            customer.wallet_decrease(drink.price)
            self.increase_till(drink.price)     
            customer.increase_drunkness_level(drink)  

    def sell_food_to_customer(self, food, customer):
        customer.wallet_decrease(food.price)
        self.increase_till(food.price)
        customer.decrease_drunkness_level(food)


    def check_customer_age(self, customer):
        return customer.age >= 18
    
    def check_customer_drunkness(self, customer):
        return customer.drunkness_level <= 8