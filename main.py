from client import Client
from account import Account, CurrentAccount

if __name__ == '__main__':
    
    client1 = Client('Juan', 'Address')
    client1.show()
    
    account1 = CurrentAccount()
    account1.withdraw(100)
    account1.deposit(100)
    account1.withdraw(50)
    account1.show()