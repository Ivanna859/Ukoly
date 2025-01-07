class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self._account_number = str(account_number)
        self._owner = owner
        self._balance = balance

    @property
    def account_number(self): return self._account_number

    @property
    def owner(self): return self._owner

    @property
    def balance(self): return self._balance

    def deposit(self, amount):
        if amount <= 0: raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"{amount} deposited. New balance: {self._balance}.")

    def withdraw(self, amount):
        if amount <= 0: raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance: raise ValueError("Insufficient funds.")
        self._balance -= amount
        print(f"{amount} withdrawn. New balance: {self._balance}.")

    def print_balance(self):
        print(f"Current balance for account {self._account_number}: {self._balance}.")

# Example usage
if __name__ == "__main__":
    account = BankAccount(123456789, "Iva Dan", 1000.0)
    account.print_balance()
    account.deposit(500.0)
    account.withdraw(200.0)
    account.print_balance()
