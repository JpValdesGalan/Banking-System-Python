import os
from client import Client

''' Bank Class '''
# Client Factory
class Bank:
    
    # Aqui guardamos la unica instancia permitida
    _INSTANCE = None
    
    ''' Bank Cosntructor '''
    def __init__(self) -> None:
        if Bank._INSTANCE == None:
            Bank._INSTANCE = self
            self.client_list = []
        else:
            print('Ya existe un Banco')
        
    def logout(self) -> None:
        Bank._INSTANCE = None
        
    def create_client(self) -> Client:
        ''' Create and adds new Client to the Bank Wallet '''
        print('Adding new Client...')
        name = str(input('Introduce Client name: '))
        address = str(input('Introduce Client address: '))
        phone = str(input('Introduce Client phone: '))
        client = Client(name, address, phone)
        print()
        self.client_list.append(client)
        
        return client
    
    def show_client(self) -> None:
        ''' Asks for an id and prints the detail of the Client by ID'''
        id = int(input('Introduce the id of the client to search: '))
        try:
            client = self.client_list[id-1]
        except:
            client = None
        if client == None:
            print(f'Invalid Client Id')
            return
        print()
        client.show()
        client.show_account_list()
    
    def show_client_list(self) -> None:
        ''' Prints the details of the Bank Clients '''
        print(f'-------------------------\n'
              f'Bank Clients List\n'
              f'-------------------------\n')
        for client in self.client_list:
            client.show()
        print(f'-------------------------\n')
    
# class Bank:
    
#     ''' Bank Constructor '''
#     def __init__(self) -> None:
#         '''  '''
#         self.client_list = []
#         self.account_list = []
        
#     ''' Bank Methods '''
#     def add_client(self, new_client: Client) -> None:
#         ''' Adds a Client to the Bank wallet '''
#         self.client_list.append(new_client)
        
#     def remove_client(self, client: Client) -> None:
#         ''' Removes a Client of the Bank wallet '''
#         self.client_list.remove(client)
#         del client
    
#     def add_account(self, new_account: Account) -> None:
#         ''' Adds an Account to the Bank Wallet '''
#         self.account_list.append(new_account)
    
#     def remove_account(self, account: Account) -> None:
#         ''' Removes an Account from the Bank Wallet '''
#         self.account_list.remove(account)
#         del account

#     def show_client_list(self) -> None:
#         ''' Prints the list of Clients in Bank Wallet '''
#         for client in self.client_list:
#             print(client.show())
    
#     def show_account_list(self) -> None:
#         ''' Prints the list of Accounts in Bank Wallet '''
#         for account in self.account_list:
#             print(account.show())
            
#     def create_client() -> Client:
#         pass
        
#     def create_account() -> Account:
#         pass