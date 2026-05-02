
class Account():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        return ("The amount deposited is :",amount)
    
    def withdrawel(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return ("The amount withdrawn is :",amount)
 
    def balance(self):
        return self.balance
    
    def get_info(self):
        return f'''Name :{self.name},\n balance:{self.balance}'''
    
class Manager():
    def __init__(self):
        self.accounts=[]
        
    def add_account(self,account):
        return self.accounts.append(account)
    
    def show_all(self):
        for account in self.accounts:
                  print(account.get_info())
            
    def max_balance(self):
        return max(self.accounts,key=lambda a:a.balance)
    
a1=Account("Farhad",10_000)
a1.deposit(10_000)
a1.withdrawel(2_000)
print("Balance of a1:",a1.balance)
a2=Account("Raafi",20_000)
a3=Account("Ata",30_000)

acc=Manager()
acc.add_account(a1)
acc.add_account(a2)                
acc.add_account(a3)        
(acc.show_all())
print(acc.max_balance().get_info())  

      
