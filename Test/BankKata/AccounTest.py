import unittest

from BankKata.Account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("101", "Legit", "4444", 2000.0)


    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance("4444"), 2000.0)
        with self.assertRaises(ValueError):
            Account("101", "Legit", "4445", 2000.0)
            with self.assertRaises(ValueError):
                Account("101", "Legit", "44456", -2000.0)


    def test_deposit(self):
        self.account.deposit(1000.0)
        self.assertEqual(self.account.get_balance("4444"), 1000.0)
        with self.assertRaises(ValueError):
            self.account.deposit(-1000.0)
        with self.assertRaises(ValueError):
            self.account.deposit(0.0)


    def test_withdraw(self):
        self.account.withdraw(1000.0)
        self.assertEqual(self.account.get_balance("4444"), 1000.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-1000.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(0.0)

