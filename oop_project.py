from bank_accounts import *

Dave = Bank_account(1000, "Dave")
Sara = Bank_account(2000, "Sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(300)

Dave.withdraw(8000)
Dave.withdraw(150)

Sara.transfer(12000, Dave)
Sara.transfer(900, Dave)

Greg = InterestRewardsAcct(1000, "Greg")

Greg.get_balance()

Greg.deposit(100)

Greg.transfer(100, Dave)