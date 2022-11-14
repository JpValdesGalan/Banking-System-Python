
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