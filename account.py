from abc import ABC, abstractmethod

''' Account Interface '''
class Account(ABC):
    
    id_counter = 1 # Keeps track of ids
    
    ''' Account Constructor '''
    def __init__(self, balance: float = 0) -> None:
        ''' Defines the account values '''
        self.id = Account.id_counter
        self.balance = balance
        
    ''' Get Methods '''
    def get_id(self) -> str:
        ''' Returns the Account id '''
        return self.id
    
    def get_balance(self) -> str:
        ''' Returns the Account balance '''
        
    ''' Account methods '''
    def deposit(self, value) -> None:
        '''  '''
        if value <= 0:
            print(f'${value:.2f} value can\'t be deposit\n')
            return
        
        self.balance += value
        print(f'${value:.2f} Deposit Succesfull\n'
              f'New Balance: ${self.balance:.2f}\n')
    
    @abstractmethod
    def withdraw(self) -> None:
        ''' Abstract Method '''
        pass
    
    @abstractmethod
    def show(self) -> None:
        ''' Abstract Method '''
        pass
    
''' CurrentAccount Class '''
class CurrentAccount(Account):
    ''' CurrentAccount Methods'''
    def withdraw(self, value) -> None:
        '''  '''
        if value > self.balance:
            print('Not enough balance on account\n')
            return
        
        self.balance -= value
        print(f'${value:.2f} Withdraw Succesfull\n'
              f'New Balance: ${self.balance:.2f}\n')
        
    def show(self) -> None:
        print(f'Current Account\n'
              f'Account No.: {self.id:06}\n'
              f'Balance: ${self.balance:.2f}\n')
    
''' SavingAccount Class '''
class SavingAccount(Account):
    ''' CurrentAccount Methods'''
    def withdraw(self) -> None:
        print('Can\'t Withdraw from a Saving Account')
        
    def show(self) -> None:
        print(f'Saving Account\n'
              f'Account No.: {self.id:06}\n'
              f'Balance: ${self.balance:.2f}\n')