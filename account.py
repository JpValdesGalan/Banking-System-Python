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
        
# class Account(ABC):
    
#     id_counter = 1 # Keeps track of ids
    
#     ''' Account Constructor '''
#     def __init__(self, balance: float = 0) -> None:
#         ''' Defines the account values '''
#         self.id = Account.id_counter
#         self.balance = balance
#         Account.id_counter += 1
        
#     ''' Get Methods '''
#     def get_id(self) -> str:
#         ''' Returns the Account id '''
#         return self.id
    
#     def get_balance(self) -> str:
#         ''' Returns the Account balance '''
        
#     ''' Account methods '''
#     def deposit(self, value) -> None:
#         '''  '''
#         if value <= 0:
#             print(f'${value:.2f} value can\'t be deposit\n')
#             return
        
#         self.balance += value
#         print(f'${value:.2f} Deposit Succesfull\n'
#               f'New Balance: ${self.balance:.2f}\n')
    
#     @abstractmethod
#     def withdraw(self) -> None:
#         ''' Abstract Method '''
    
#     @abstractmethod
#     def show(self) -> None:
#         ''' Abstract Method '''
    
# ''' CurrentAccount Class '''
# class CurrentAccount(Account):
#     ''' CurrentAccount Methods'''
#     def withdraw(self, value) -> None:
#         '''  '''
#         if value > self.balance:
#             print('Not enough balance on account\n')
#             return
        
#         self.balance -= value
#         print(f'${value:.2f} Withdraw Succesfull\n'
#               f'New Balance: ${self.balance:.2f}\n')
        
#     def show(self) -> None:
#         print(f'Current Account\n'
#               f'Account No.: {self.id:06}\n'
#               f'Balance: ${self.balance:.2f}\n')
    
# ''' SavingAccount Class '''
# class SavingAccount(Account):
#     ''' CurrentAccount Methods'''
#     def withdraw(self, value) -> None:
#         print('Can\'t Withdraw from a Saving Account\n')
        
#     def show(self) -> None:
#         print(f'Saving Account\n'
#               f'Account No.: {self.id:06}\n'
#               f'Balance: ${self.balance:.2f}\n')