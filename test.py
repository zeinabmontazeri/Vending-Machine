import unittest
from vendingMachine import VendingMachine, Coin


class VendingMachineTest(unittest.TestCase):

    def setUp(self):
        self.vending_machine = VendingMachine()

    def tearDown(self):
        pass

    def test_insert_coin(self):
        self.vending_machine.insert_coin(Coin(0.10))
        self.assertEqual(0.10, self.vending_machine.get_credit(), "The credit is the same as the inserted coin")

    def test_get_credit(self):
        self.vending_machine.insert_coin(Coin(0.10))
        self.vending_machine.insert_coin(Coin(0.25))
        self.vending_machine.insert_coin(Coin(0.50))
        self.assertEqual(0.85, self.vending_machine.get_credit(), "The credit matches the sum of the inserted coins")

    def test_successful_purchase_with_enough_credit(self):
        self.vending_machine.insert_coin(Coin(1.0))
        self.vending_machine.insert_coin(Coin(0.50))
        self.vending_machine.insert_coin(Coin(0.10))
        self.vending_machine.insert_coin(Coin(0.10))

        self.assertEqual(True, self.vending_machine.purchase(1.70), "Purchase is successful with sufficient credit.")

    def test_remaining_money_at_successful_purchase(self):
        self.vending_machine.insert_coin(Coin(1.0))
        self.vending_machine.insert_coin(Coin(0.50))
        self.vending_machine.insert_coin(Coin(0.10))
        self.vending_machine.insert_coin(Coin(0.10))
        self.vending_machine.insert_coin(Coin(0.05))
        self.vending_machine.purchase(1.70)

        self.assertEqual(0.05, self.vending_machine.get_credit(), "The credit matches remaining money after purchase")

    def test_unsuccessful_purchase_with_not_enough_credit(self):
        self.vending_machine.insert_coin(Coin(1.0))
        self.vending_machine.insert_coin(Coin(0.50))
        self.vending_machine.insert_coin(Coin(0.10))

        self.assertEqual(False, self.vending_machine.purchase(1.70), "Purchase is failed with insufficient credit.")
