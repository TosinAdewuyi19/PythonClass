import unittest
from BankKata.Bank import Bank
from BankKata.Account import Account

class TestBank(unittest.TestCase):
    def setUp(self):
        """Set up a bank and accounts for testing."""
        self.bank = Bank("TestBank")
        self.account = Account("1000", "Tosin", "password122")
        self.account1 = Account("1001", "Alice", "password123", 1000.0)
        self.account2 = Account("1002", "Bob", "password456", 500.0)
        self.bank.add_account(self.account1)
        self.bank.add_account(self.account2)

    def test_add_account(self):
        """Test adding accounts to the bank."""
        self.assertEqual(len(self.bank.accounts), 2)
        with self.assertRaises(ValueError):
            self.bank.add_account(Account("1001", "Charlie", "password789"))  # Duplicate account number

    def test_find_account(self):
        """Test finding an account by account number."""
        account = self.bank.find_account_by_account_number("1001")
        self.assertEqual(account.account_holder_name, "Alice")
        with self.assertRaises(ValueError):
            self.bank.find_account_by_account_number("9999")  # Account not found

    def test_deposit(self):
        """Test depositing into an account."""
        self.bank.deposit("1001", 200.0)
        self.assertEqual(self.bank.get_balance("1001"), 1200.0)
        with self.assertRaises(ValueError):
            self.bank.deposit("1001", -100.0)  # Negative deposit
        with self.assertRaises(ValueError):
            self.bank.deposit("1001", 0.0)  # Zero deposit

    def test_withdraw(self):
        """Test withdrawing from an account."""
        self.bank.withdraw("1002", 100.0, "password456")
        self.assertEqual(self.bank.get_balance("1002"), 400.0)
        with self.assertRaises(ValueError):
            self.bank.withdraw("1002", 1000.0, "password456")  # Insufficient funds
        with self.assertRaises(ValueError):
            self.bank.withdraw("1002", -50.0, "password456")  # Negative withdrawal
        with self.assertRaises(ValueError):
            self.bank.withdraw("1002", 0.0, "password456")  # Zero withdrawal
        with self.assertRaises(ValueError):
            self.bank.withdraw("1002", 100.0, "wrongpassword")  # Invalid password

    def test_get_balance(self):
        """Test retrieving the balance of an account."""
        self.assertEqual(self.bank.get_balance("1001"), 1000.0)
        with self.assertRaises(ValueError):
            self.bank.get_balance("1001", "wrongpassword")  # Invalid password

    def test_update_password(self):
        """Test updating the password of an account."""
        self.assertTrue(self.bank.update_password("1001", "password123", "newpassword123"))
        self.assertEqual(self.bank.get_balance("1001", "newpassword123"), 1000.0)
        with self.assertRaises(ValueError):
            self.bank.update_password("1001", "wrongpassword", "newpassword123")  # Invalid old password
        with self.assertRaises(ValueError):
            self.bank.update_password("1001", "newpassword123", "123")  # Invalid new password (too short)

    def test_invalid_account_operations(self):
        """Test operations on invalid accounts."""
        with self.assertRaises(ValueError):
            self.bank.deposit("9999", 100.0)  # Account not found
        with self.assertRaises(ValueError):
            self.bank.withdraw("9999", 100.0, "password123")  # Account not found
        with self.assertRaises(ValueError):
            self.bank.get_balance("9999")
        with self.assertRaises(ValueError):
            self.bank.update_password("9999", "password123", "newpassword123")  # Account not found

if __name__ == "__main__":
    unittest.main()