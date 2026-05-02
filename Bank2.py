

# from abc import ABC ,abstractmethod
 
# class Account(ABC):
#     def __init__(self,account,balance):
#         self.account=account
#         self.balance=balance    
        
#     @abstractmethod
#     def get_details(self):
#         pass
    
# class SavingsAccount(Account):
#     def __init__(self,account,balance,interest):  # what does it OWN?
#         super().__init__(account,balance)  # what does it need from parent?
#         self.interest=interest                    # what's new?
    
#     def get_details(self):     # what does it DO?
#         return f'''account:{self.account}
#                   balance:{self.balance}
#                   interest:{self.interest}
#                   '''
    
#     def add_interest(self):    
#         self.balance += self.balance * self.interest
#         return f" The balance after interest is {self.balance}"
        
        
# class CurrentAccount(Account):
#     def __init__(self,account,balance,overdraft_limit):
#         super().__init__(account,balance)  # what does it need from parent?
#         self.overdraft_limit=overdraft_limit
        
#     def get_details(self):     # what does it DO?
#         return f'''account:{self.account}
#                   balance:{self.balance}
#                   overdraft_limit:{self.overdraft_limit}
#                   '''
                  
#     def withdraw(self,amount):
#         if amount <= self.balance + self.overdraft_limit:
#             self.balance-=amount
#             return (f"The amount limit of overdraft is {self.overdraft_limit}")
#         else:
#             return ("insufficient balance")  
        
# class Bank():
#     def __init__(self):
#         self.account=[]
        
#     def add_accounts(self,account):
#         return self.account.append(account)
        
#     def show_all(self):
#         for i in self.account:
#             print(f"{i.get_details()}")
            
#     def balance(self):
#         return sum(account.balance for account in self.account)
        
# s1=SavingsAccount(2005,5000,.10)
# print(s1.get_details())
# print(s1.add_interest())


# c1=CurrentAccount(2006,6000,4000)
# print(c1.get_details())
# print(c1.withdraw(5000))

# bank = Bank()
# bank.add_accounts(s1)
# bank.add_accounts(c1)
# bank.show_all()
# print(bank.balance())
