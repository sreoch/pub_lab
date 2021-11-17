class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    
    def increase_till(self, amount):
        self.till += amount
    
    def add_drink(self, drink):
        self.drinks.append(drink)
    
    def stock_count(self):
        return len(self.drinks)

    def sell_drink_to_customer(self, drink, customer):
        if self.check_customer_age:
            customer.wallet_decrease(drink.price)
            self.increase_till(drink.price)
        


    def check_customer_age(self, customer):
        return customer.age >= 18