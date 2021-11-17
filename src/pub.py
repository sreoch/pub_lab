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

    def sell_drink_to_customer(self, amount, customer):
        customer.wallet_decrease(amount)
        self.increase_till(amount)