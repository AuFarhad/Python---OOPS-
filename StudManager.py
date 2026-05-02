class Student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    def get_info(self):
            return f'''name:{self.name}
                   roll_no:{self.roll_no}
                   marks:{self.marks}
                   '''
                   
class StudentManager():
    def __init__(self):
        self.students=[]
        
    def add_students(self,student):
        self.students.append(student)
        
    def show_all(self):
        for student in self.students:
            print(student.get_info())
        
    def search(self):
        for student in self.students:
            if student.name =="Farhad":
                print(student.get_info())
                return
        print("not found")       
         
    def max_marks(self):
        return max(self.students,key=lambda s:s.marks)
    
s1=(Student("Farhad",123,99))
s2=(Student("arhad",124,89))
s3=(Student("had",125,79))

stud=StudentManager()
stud.add_students(s1)
stud.add_students(s2)
stud.add_students(s3)

stud.show_all()
stud.search()
print(stud.max_marks().get_info())
