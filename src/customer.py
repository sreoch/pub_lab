class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def wallet_decrease(self, amount):
        self.wallet -= amount