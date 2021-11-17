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
        if self.check_customer_age(customer) and self.check_customer_drunkness(customer):
            customer.wallet_decrease(drink.price)
            self.increase_till(drink.price)
            customer.increase_drunkness_level(drink.alcohol_level)
        

    def check_customer_age(self, customer):
        return customer.age >= 18
    
    def check_customer_drunkness(self, customer):
        return customer.drunkness_level <= 8