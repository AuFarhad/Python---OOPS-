
class Todo():
    def __init__(self,title,time,todo):
        self.title=title
        self.time=time
        self.todo=todo
         
    def get_info(self):
        return f"Title:{self.title}\nTime:{self.time}\n{self.todo} "
    
    
class TodoList():
    def __init__(self):
        self.todos=[]
        
    def add_list(self,todo):
        self.todos.append(todo)

    def show_all (self):
        for todo in self.todos:
            print(todo.get_info())
            
t1=Todo("Writing","5 pm","Completing the unheard poem,Practice Essay")
t2=Todo("Reading","6 pm ","Completing the book (The love my life)")
t3=Todo("Coding","7 pm - 10 pm " ,"Numpy(1-hr),Pandas(1-hr),Revision(1-hr)")

       
t=TodoList()

t.add_list(t1)
t.add_list(t2)
t.add_list(t3)

t.show_all()
