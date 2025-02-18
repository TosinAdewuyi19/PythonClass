from os import environ

'import-module environ'


class Account:
    def __init__(self, account_number, account_holder_name, pin, balance=0.0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        if not(isinstance(pin, str) or len(pin) != 4 or not pin.isdigit()):
            raise TypeError("Pin must be a 4-digit integer.")
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.pin = pin
        self.balance = balance


    def verify_pin(self, pin):
        if pin != self.pin:
            raise ValueError("Pin does not match")
        return self.pin == pin

    def update_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            raise ValueError("Invalid old pin")
        if not isinstance(self.pin, str) or len(self.pin) != 4 or not new_pin.isdigit():
            raise TypeError("Pin must be a 4-digit integer.")
        self.pin = new_pin
        return True

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit  amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            raise ValueError("Invalid Pin")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("INSUFFICIENT FUNDS")
        self.balance -= amount
        return self.balance

    def get_balance(self, pin):
        if pin != self.pin:
            raise ValueError("Invalid Pin")
        return self.balance

    def __str__(self):
        return f"Account(account_number={self.account_number}, account_holder_name={self.account_holder_name}, balance={self.balance})"

