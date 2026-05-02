
        
        
from abc import ABC,abstractmethod

class Product(ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    @abstractmethod
    def get_info(self):
        pass
    
class Electronic(Product):
    def __init__(self,name,price,warranty):
        super().__init__(name,price)
        self.warranty=warranty
        
    def get_info(self):
        return f'''name:{self.name}
                   price:{self.price}
                   warranty:{self.warranty}'''
                   
                   
    def __str__(self):        
        return f'''name:{self.name}
                   price:{self.price}
                   warranty:{self.warranty}'''
                   
    def __mul__(self,quantity):
        return self.price*quantity
    
class clothes(Product):
    def __init__(self,name,price,size):
        super().__init__(name,price)
        self.size=size
        
    def get_info(self):
        return f'''name:{self.name}
                   price:{self.price}
                   size:{self.size}
                   '''
                   
class Cart():
    def __init__(self):
        self.Product=[]
        
    def add_product(self,product):
        self.Product.append(product)
        
    def show_cart(self):
        for i in self.Product:
            print(i.get_info())
            
                
    def total_prices(self):
        return sum(product.price for product in self.Product)
    
    def most_expensive(self):
       return max(self.Product, key=lambda p: p.price)
                 
e1 = Electronic("Laptop", 50000, 2)
e2 = Electronic("Phone", 20000, 1)
c1 = clothes("Shirt", 1000, "L")

cart = Cart()
cart.add_product(e1)
cart.add_product(e2)
cart.add_product(c1)

cart.show_cart()
print(cart.total_prices())
print(cart.most_expensive().get_info())
print(e1 * 3)
 
 
