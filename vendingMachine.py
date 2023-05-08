class VendingMachine(object):

    def __init__(self):
        self.credit = 0
        self.price = None
        self.change = []

    def insert_coin(self, coin):
        self.credit += coin.value

    def get_credit(self):
        return round(self.credit, 2)

    def purchase(self, needed_credit):
        if self.credit >= needed_credit:
            self.credit -= needed_credit
            return True
        else:
            return False


class Coin(object):
    VALUES = (1, 0.50, 0.25, 0.10, 0.05)

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Product(object):
    VALUES = ("Coffee", "Soda")
    OPTIONS = {"0A": "Coffee", "0B": "Soda"}
    PRICE = {"Coffee": "0.75", "Soda": "0.50"}

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


# my idea: first choose product then add coin
