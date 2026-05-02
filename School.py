
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @abstractmethod
    def get_info(self):
        pass
        
class student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
        
    def get_info(self):
        return f'''The Student name is {self.name}
                   His age is {self.age}
                   His rollno is {self.rollno}
                   His marks is {self.marks}
                   '''
        
    def __str__(self):
        return f'''name:{self.name}
                   age:{self.age}
                   rollno:{self.rollno}
                   marks:{self.marks}'''
                   
    def __len__(self):
     return self.marks
    
    def __add__(self, other):
     return self.marks + other.marks
    
class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject=subject
        self.salary=salary
    
    def get_info(self):
        return f'''His/her name is {self.name}.
                   Who takes subject {self.subject}
                   Who's salary is  {self.salary}'''
                   
                   
class School():
    def __init__(self):
        self.student=[]
        self.Teacher=[]
        
    def add_student(self,student):
        return self.student.append(student)
    
    def add_teacher(self, teacher):
       self.Teacher.append(teacher)
    
    def __add__(self, other):
       return self.marks + other.marks
    
    def show_student(self):
        for student in self.student:
            print(student.get_info())
    
    def show_teacher(self):
       for teacher in self.Teacher:
          print(teacher.get_info())
    
    def top_student(self):
        return max(self.student, key=lambda s: s.marks)
    
      
s1 = student("Farhad", 20, 101, 85)
s2 = student("Raafi", 21, 102, 90)
t1 = Teacher("Mr. Khan", 35, "Maths", 50000)

school = School()
school.add_student(s1)
school.add_student(s2)
school.add_teacher(t1)

school.show_student()
school.show_teacher()
print(school.top_student().get_info())
print(s1 + s2) 


