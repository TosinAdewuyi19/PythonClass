import unittest
import bcrypt

from BankKata.Account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("101", "Legit", "legit1234", 2000.0)


    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance("legit1234"), 2000.0)


    def test_deposit(self):
        self.account.deposit(1000.0)
        self.assertEqual(self.account.get_balance("legit1234"), 3000.0)
        with self.assertRaises(ValueError):
            self.account.deposit(-1000.0)
        with self.assertRaises(ValueError):
            self.account.deposit(0.0)


    def test_withdraw(self):
        self.account.withdraw(1000.0, "legit1234")
        self.assertEqual(self.account.get_balance("legit1234"), 1000.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-1000.0, "legit1234")
        with self.assertRaises(ValueError):
            self.account.withdraw(0.0, "legit1234")


    def test_get_balance(self):
        self.assertEqual(self.account.get_balance("legit1234"), 2000.0)
        self.account.get_balance("legit1234")

if __name__ == '__main__':
    unittest.main()


