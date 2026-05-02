class Cart():
    def __init__(self):
        self.products=[]
        
    def add_product(self,product):
            for p in self.products:
                if p.name==product.name:
                    p.quantity+=product.quantity
                    return
                    
            
            
            self.products.append(product)
            
                    

    def remove_product(self,name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f"{name} removed")
                return
        print("Product not found")
                
    def show_cart(self):
        for product in self.products:
            print(product.get_info())
            
    def total_price(self):
        return sum(p.price*p.quantity for p in self.products )
    
p1=Product("Milk",20,2)
p2=Product("Cake",100,1)
p3=Product("Milk",20,2)
p4=Product("sugar",30,1)

c=Cart()
c.add_product(p1)
c.add_product(p2)
c.add_product(p3)
c.add_product(p4)
c.remove_product("Cake")
c.show_cart()
print(c.total_price())
