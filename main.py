from client import Client
from account import Account, SavingAccount, CurrentAccount
from bank import Bank

if __name__ == '__main__':
    
    bank1 = Bank()
    
    client1 = Client('Juan', 'Address')
    bank1.add_client(client1)
    client1.show()
    
    account1 = CurrentAccount()
    bank1.add_account(account1)
    account1.withdraw(100)
    account1.deposit(100)
    account1.withdraw(50)
    account1.show()
    
    account2 = SavingAccount()
    bank1.add_account(account2)
    account1.withdraw(100)
    account1.deposit(100)
    account1.withdraw(50)
    account1.show()
    
    bank1.show_client_list()
    bank1.show_account_list()
    