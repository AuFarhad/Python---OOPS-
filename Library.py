from abc import ABC ,abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def get_info(self):
        pass
    
class Book(LibraryItem):
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        
    def get_info(self):
        return f'''The title is {self.title} written by {self.author}.
                The total no of pages are {self.pages}''' 
     
     
    def __str__(self):
        return f'''Title:{self.title}
                   Author:{self.author}
                   pages:{self.pages}'''
                   
    def __len__(self):
        return self.pages
    
    
class magazine(LibraryItem):
    def __init__(self,title,issue,pages):
        self.title=title
        self.issue=issue
        self.pages=pages
        
    def get_info(self):
        return f"The {self.title} with the issue is {self.issue}"
    
class library():
    def __init__(self):
        self.items=[]
        
    def add_items(self,item):
        self.items.append(item)
    

    def show_all(self):
        for item in self.items:
            print(item.get_info())        
    
    def total_pages(self):
        return sum(item.pages for item in self.items)
    
    
b1 = Book("No1King", "Author1", 300)
b2 = Book("TheTrueOne", "Author2", 250)
m1 = magazine("TimesIdea", "Issue5", 50)

lib = library()
lib.add_items(b1)
lib.add_items(b2)
lib.add_items(m1)

lib.show_all()
print(lib.total_pages())
    
    
