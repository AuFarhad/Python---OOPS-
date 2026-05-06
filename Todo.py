class Todo():
    Name="Farhads Todo list"
    def __init__(self,title,time,description):
        self.title=title
        self.time=time
        self.description=description
        
    def __str__(self):
        return f"{self.Name}\nTitle:{self.title}\ntime:{self.time}\ndescription:{self.description}"
    
class Todolist():
    def __init__(self):
        self.todos=[]
        self.filename="todo.txt"
        
    def add_list(self,todo):
        self.todos.append(todo)
        
    def show_all(self):
        for todo in self.todos:
            print(str(todo))
        
    def write_file(self):
        with open(self.filename,"w") as f:
            for todo in self.todos:
                f.write(str(todo) + "\n")
        print("file created")
        
    def read_file(self):
        with open(self.filename,"r") as f:
            data=f.read()
            print("\nFile Creation\n")
            print(data)
            
t1=Todo("Writing","5 pm","Completing the unheard poem,Practice Essay")
t2=Todo("Reading","6 pm ","Completing the book (The love my life)")
t3=Todo("Coding","7 pm - 10 pm " ,"Numpy(1-hr),Pandas(1-hr),Revision(1-hr)")

       
t=Todolist()

t.add_list(t1)
t.add_list(t2)
t.add_list(t3)
(t.show_all())
t.write_file()
t.read_file()

