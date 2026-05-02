
from abc import ABC ,abstractmethod

class Payment(ABC):
    def __init__(self,amount):
        self.amount=amount
    
    @abstractmethod
    def pay(self):
        pass
    
class UPI(Payment):
    def __init__(self,amount,upi_id):
        super().__init__(amount)
        self.upi_id=upi_id
        
    def pay(self):
        return f"Your {self.amount} is credited to your cardnumber is {self.upi_id}"
    
class Card(Payment):
    def __init__(self,amount,card_number):
        super().__init__(amount)
        self.card_number=card_number
       
    def pay(self):
        return f"Your {self.amount} is credited to your cardnumber is {self.card_number}" 
    
class Cash(Payment):
    def __init__(self,amount):
        super().__init__(amount)
        
    def pay(self):
        return f"Paid {self.amount} using cash"
        
class PaymentManager():
    def __init__(self):
        self.payments=[]
        
    def add_payment(self,payment):
        self.payments.append(payment)
        
    def show_all_payments(self):
        for payment in self.payments:
            print(payment.pay())
    
    def total_amount(self):
        return sum(p.amount for p in self.payments) 
    
p1=UPI(1000,"farhad")
p2=Card(2000,"1234")
p3=Cash(500)

pm=PaymentManager()
pm.add_payment(p1)
pm.add_payment(p2)
pm.add_payment(p3)

pm.show_all_payments()
print("Total:",pm.total_amount())
