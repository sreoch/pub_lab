class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness_level = 0

    def wallet_decrease(self, amount):
        self.wallet -= amount

    def increase_drunkness_level(self, drink):
        self.drunkness_level += drink.alcohol_level