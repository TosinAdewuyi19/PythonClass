import bcrypt


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Account:
    def __init__(self, account_number, account_holder_name, password, balance=0.0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        if not(isinstance(password, str) or len(password) != 8 or not password.isdigit()):
            raise TypeError("Pin must be a 4-digit integer.")
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.password_hash = hash_password(password)
        self.balance = balance


    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)


    def update_password(self, old_password, new_password):
        if not self.verify_password(old_password):
            raise ValueError("Invalid password")
        if not isinstance(new_password, str) or len(new_password) != 8:
            raise ValueError("New password must be at least 8 characters long.")
        self.password_hash = hash_password(new_password)
        return True


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit  amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount, password):
        if not self.verify_password(password):
            raise ValueError("Invalid Password")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("INSUFFICIENT FUNDS")
        self.balance -= amount
        return self.balance

    def get_balance(self, password):
        if not self.verify_password(password):
            raise ValueError("Invalid Password")
        return self.balance



    def __str__(self):
        return f"Account(account_number={self.account_number}, account_holder_name={self.account_holder_name}, balance={self.balance})"





