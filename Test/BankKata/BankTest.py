import unittest

from Bank import Bank


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("TestBank")
        self.account1 = Account("101", "Legit", 2000.0)
        self.account2 = Acoount("102", "Tosin", 2500.0)
        self.bank.add_account(self.account1)
        self.bank.add_account(self.account2)

    def test_create_account(self):
        self.assertEqual(self.bank.create_account(self.account1), "101")
        with self.assertRaises(ValueError):
            self.bank.create_account(Account("101", "Legit"))


    def test_find_account_by_account_number(self):
        account = self.bank.find_account_by_account_number("101")
        self.assertEqual(account.account_holder_name, "Legit")
        with self.assertRaises(ValueError):
            self.bank.find_account_by_account_number("101")


    def test_deposit(self):
        self.bank.deposit("101", 1500.0)
        self.assertEqual(self.bank.get_balance("101"), 3500.0)
        with self.assertRaises(ValueError):
            self.bank.deposit("101", -100.0)
        with self.assertRaises(ValueError):
            self.bank.deposit("101", 0.0)

    def test_withdraw(self):
        self.bank.withdraw("102", 1500.0)
        self.assertEqual(self.bank.get_balance("102"), 2500.0)
        with self.assertRaises(ValueError):
            self.bank.withdraw("102", -100.0)
        with self.assertRaises(ValueError):
            self.bank.withdraw("102", 0.0)
        with self.assertRaises(ValueError):
            self.bank.withdraw("102", 3000.0)


    def test_get_balance(self):
        self.assertEqual(self.bank.get_balance("101"), 3500.0)
        self.assertEqual(self.bank.get_balance("102"), 2500.0)


    def test_transfer(self):
        self.bank.transfer_money("101", 1500.0, 2000.0)
        self.assertEqual(self.bank.get_balance("102"), 2500.0)
        with self.assertRaises(ValueError):
            self.bank.transfer_money("101", -100.0, 2000.0)
        with self.assertRaises(ValueError):
            self.bank.transfer_money("101", 0.0, 2000.0)
        with self.assertRaises(ValueError):
            self.bank.transfer_money("101", 3000.0, 2000.0)

if __name__ == '__main__':
    unittest.main()



