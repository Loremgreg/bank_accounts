class BalanceException(Exception):
    pass


class Bank_account:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.account_name = account_name
        print(f"\nAccount '{self.account_name}' created. \n Balance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.account_name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if amount <= self.balance:
            return
        else:
            raise BalanceException(f"\Sorry, account '{self.account_name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"\n✅ Transaction accepted, you have withdraw ${amount}")
            self.get_balance()
        except BalanceException as error:
            print(f"\n❌ Withdraw interrupted: {error}")


    def transfer():
        pass