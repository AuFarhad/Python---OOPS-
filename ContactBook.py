class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
        
    def get_info(self):
        return f'''name:{self.name},
                   phone:{self.phone}
                   email:{self.email}
                   '''

class ContactBook:
    def __init__(self):
     self.contacts=[]
    
    def add_contact(self,contact):
     self.contacts.append(contact)
    
    def show_all(self):
     for contact in self.contacts:
        print(contact.get_info())
    
    def search(self):
     for contact in self.contacts:
        if contact.name == "Farhad":
            print(contact.name)    
            
    def delete(self):
     for contact in self.contacts:
        if contact.name == "had":
            self.contacts.remove(contact)
            print("deleted :",contact.name) 
        
    def save_to_file(self):
     with open("p.txt","w")as f:
        for contact in self.contacts:
          f.write(f"{contact.name} ,{contact.phone} ,{contact.email} \n")
               
    def load_from_file(self):
     with open("p.txt","r")as f:
        print(f.read())
        
c1=Contact("Farhad",9035,"auf@1234")
c2=Contact("arhad",9036,"uf@1234")
c3=Contact("had",9033,"f@1234")

cont=ContactBook()
cont.add_contact(c1)
cont.add_contact(c2)
cont.add_contact(c3)

cont.show_all()
(cont.search())
(cont.delete())
(cont.save_to_file())
(cont.load_from_file())
