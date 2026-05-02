

class Calc():
    def __init__(self,val_1,val_2):
        self.val_1=val_1
        self.val_2=val_2
        
    def get_info(self):
        return f"The First value is {self.val_1}.\nThe second value is {self.val_2}"
         
    def add(self):
          return f"The Additon for {self.val_1} and {self.val_2} is :{self.val_1+self.val_2}"
    
    def sub(self):
        return f"The Subtraction  for {self.val_1} and {self.val_2} is :{self.val_1-self.val_2}"
    
    def mul(self):
        return f"The Multiplication for {self.val_1} and {self.val_2} is :{self.val_1*self.val_2}"
    
    def div(self):
        return f"The Division for {self.val_1} and {self.val_2} is :{self.val_1/self.val_2}" 
    
    def mod(self):
        return f"The Modulus for {self.val_1} and {self.val_2} is :{self.val_1%self.val_2}"
  
while True:
       print("Welcome to calculator")
       print("Choose a format to calculate : ")
       print(''' 1.Addition(+) \n 2.Subtraction(-) \n 3.Multiplication(*) \n 4.Division(/) \n 5.Modulus(%) \n 6.Exit''')
       Choice=int(input("Choose an option :"))
       val_1=float(input("Whats the first value :"))
       val_2=float(input("Whats the Second value :"))
       c1=Calc(val_1,val_2)
       if Choice==1:
        print(c1.add())
       elif Choice==2:
           print(c1.sub())
       elif Choice==3:
         print(c1.mul())
       elif Choice==4:
         print(c1.div())
       elif Choice==5:
         print(c1.mod())
       elif Choice==6:
           print("The calculation has been exited")
           break
       else:
           print("Error")
                    
