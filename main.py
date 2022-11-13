
from bank import Bank

if __name__ == '__main__':
    
    bank = Bank()
    bank_copy = Bank()
    
    client1 = bank.create_client()
    account1 = client1.create_account()
    account2 = client1.create_account()
    
    client1.show_account_list()
    
    client2 = bank.create_client()
    account3 = client2.create_account()
    
    client2.show_account_list()
    
    bank.show_client_list()
    bank.show_client()
    
    
    # for account in client1.account_list:
    #     print(account.show())
    
    # client1 =  Client('Juan', 'Address Sample', '8712808363')
    # client1.show()
    
    # account1 = SavingAccount()
    # account1.deposit(100)
    # account1.withdraw(50)
    # account1.show()
    
    # account2 = CurrentAccount(100)
    # account2.deposit(100)
    # account2.withdraw(100)
    # account2.show()
    
    # --------------------------------------------------
    # bank1 = Bank()
    
    # client1 = Client('Juan', 'Address', '8712808363')
    # bank1.add_client(client1)
    # client1.show()
    
    # account1 = CurrentAccount()
    # bank1.add_account(account1)
    # account1.withdraw(100)
    # account1.deposit(100)
    # account1.withdraw(50)
    # account1.show()
    
    # account2 = SavingAccount()
    # bank1.add_account(account2)
    # account1.withdraw(100)
    # account1.deposit(100)
    # account1.withdraw(50)
    # account1.show()
    
    # bank1.show_client_list()
    # bank1.show_account_list()
    