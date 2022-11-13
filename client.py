import os
from account import Account, SavingAccount, CurrentAccount

''' Client Class '''
# Bank's product and Account Factory
class Client:
    
    id_counter = 1
    
    ''' Client Constructor '''
    def __init__(self, name: str, address: str, phone: str) -> None:
        self.id = Client.id_counter
        self.name = name
        self.address = address
        self.phone = phone
        self.account_list = []
        Client.id_counter += 1
        
    ''' Client Get Methods '''
    def get_name(self) -> str:
        return self.name

    def get_address(self) -> str:
        return self.address
    
    def get_phone(self) -> str:
        return self.phone
    
    ''' Client Set Methods '''
    def set_name(self, new_name) -> str:
        self.name = new_name
        
    def set_address(self, new_address) -> str:
        self.address = new_address
    
    def set_phone(self, new_phone) -> str:
        self.phone = new_phone
        
    ''' Client Methods '''
    def show(self) -> None:
        ''' Prints the details of the Client '''
        print(f'Cliente\n'
              f'Id: {self.id:06}\n'
              f'Name: {self.name}\n'
              f'Address: {self.address}\n'
              f'Phone Number: {self.phone}\n')
            
    def create_account(self) -> Account:
        ''' Create and adds a new Account to the Client Wallet '''
        print('Creating New Account...')
        type = str(input('Type of Account (S/C): '))
        balance = float(input('Initial Credit: $'))
        if type.lower() == 's':
            account = SavingAccount(balance)
        elif type.lower() == 'c':
            account = CurrentAccount(balance)
        else:
            print('Invalid Account Type\n')
            return
        self.account_list.append(account)
        print()
        return account
    
    def show_account_list(self) -> None:
        ''' Prints the details of the Client Accounts '''
        print(f'-------------------------\n'
              f'{self.name} Accounts list\n'
              f'-------------------------\n')
        for account in self.account_list:
            account.show()
        print(f'-------------------------\n')
    
# class Client:
    
#     id_counter = 1 # Keeps track of ids
    
#     ''' Client Constructor '''
#     def __init__(self, name: str, address: str) -> None:
#         ''' Defines the Client values'''
#         self.id = Client.id_counter
#         self.name = name
#         self.address = address
#         Client.id_counter += 1
        
#     ''' Get Methods '''
#     def get_id(self) -> str:
#         ''' Returns the Client id '''
#         return self.id
    
#     def get_name(self) -> str:
#         ''' Returns the Client name '''
#         return self.name
    
#     def get_address(self) -> str:
#         ''' Returns the Client address '''
#         return self.address
    
#     ''' Set Methods'''
#     def set_name(self, new_name) -> None:
#         ''' Updates the Client name value '''
#         self.name = new_name
        
#     def set_address(self, new_address) -> None:
#         ''' Updates the Client address value '''
#         self.address = new_address
        
#     ''' Client Methods '''
#     def show(self) -> None:
#         ''' The show method prints the details of the Client '''
#         print(f'Cliente\n'
#               f'Id: {self.id:06}\n'
#               f'Name: {self.name}\n'
#               f'Address: {self.address}\n')