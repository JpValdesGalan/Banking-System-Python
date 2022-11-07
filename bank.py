from client import Client
from account import Account, SavingAccount, CurrentAccount

''' Bank Class '''
class Bank:
    
    ''' Bank Constructor '''
    def __init__(self) -> None:
        '''  '''
        self.client_list = []
        self.account_list = []
        
    ''' Bank Methods '''
    def add_client(self, new_client: Client) -> None:
        ''' Adds a Client to the Bank wallet '''
        self.client_list.append(new_client)
        
    def remove_client(self, client: Client) -> None:
        ''' Removes a Client of the Bank wallet '''
        self.client_list.remove(client)
        del client
    
    def add_account(self, new_account: Account) -> None:
        ''' Adds an Account to the Bank Wallet '''
        self.account_list.append(new_account)
    
    def remove_account(self, account: Account) -> None:
        ''' Removes an Account from the Bank Wallet '''
        self.account_list.remove(account)
        del account

    def show_client_list(self) -> None:
        ''' Prints the list of Clients in Bank Wallet '''
        for client in self.client_list:
            print(client.show())
    
    def show_account_list(self) -> None:
        ''' Prints the list of Accounts in Bank Wallet '''
        for account in self.account_list:
            print(account.show())