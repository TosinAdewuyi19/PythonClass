class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}


    def create_account(self, account):
        if account.account_number in self.accounts:
            raise ValueError("Account number already exists")
        self.accounts[account.account_number] = account


    def find_account_by_account_number(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist")
        return self.accounts[account_number]

    def deposit(self, account_number, amount):
        account = self.find_account_by_account_number(account_number)
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist")
        return account.deposit(amount)

    def withdraw(self, account_number, amount):
        account = self.find_account_by_account_number(account_number)
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist")
        return self.accounts[account_number].withdraw(amount)

    def get_balance(self, account_number):
        account = self.find_account_by_account_number(account_number)
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist")
        return account.get_balance

    def transfer_money(self, account_number, amount, from_account_number, to_account_number):
        account = self.find_account_by_account_number(account_number)
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist")
        return account.transfer_money(amount, from_account_number, to_account_number)


    def __str__(self):
        return f"Bank(name={self.name}, accounts={len(self.accounts)})"
