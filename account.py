import os
from abc import ABC, abstractmethod

''' Account Interface '''
# Client Product
class Account(ABC):
    
    id_counter = 1
    
    ''' Account Constructor '''
    def __init__(self, balance: float = 0) -> None:
        self.id = Account.id_counter
        self.balance = balance
        Account.id_counter += 1
        
    ''' Account Get Methods '''
    def get_balance(self) -> float:
        return self.balance
    
    ''' Account Methods '''
    def deposit(self, value) -> None:
        ''' Deposit a quantity to the Acccount balance '''
        if not isinstance(value, float):
            print(f'Deposit Failed\n'
                  f'Value({value}) must be float')
        if value <= 0:
            print(f'Deposit Failed\n'
                  f'Value({value}) must be greater or equal to Zero(0)')
        self.balance += value
            
    def withdraw(self, value) -> None:
        ''' Withdraw a quantity from the Acccount balance '''
        if not isinstance(value, float):
            print(f'Withdraw Failed\n'
                  f'Value({value}) must be float')
        if value > self.balance:
            print(f'Withdraw Failed\n'
                  f'Value({value}) must be greater than Account balance({self.balance})')
        self.balance -= value
        
    
    @abstractmethod
    def show(self) -> None:
        ''' Show Abstract Method '''
       
# Client Product A 
''' Current Account Class '''
class CurrentAccount(Account):
    def show(self) -> None:
        ''' Prints Current Account details '''
        print(f'Current Account\n'
              f'Account No.: {self.id:06}\n'
              f'Balance: ${self.balance:.2f}\n')

# Client Product B
''' Saving Account Class '''
class SavingAccount(Account):
    def show(self) -> None:
        ''' Prints Saving Acount details'''
        print(f'Saving Account\n'
              f'Account No.: {self.id:06}\n'
              f'Balance: ${self.balance:.2f}\n')