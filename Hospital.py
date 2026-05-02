
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @abstractmethod 
    def get_info(self):
        pass
    
class Patient(Person):
    def __init__(self,name,age,disease,room_no):
        super().__init__(name,age)
        self.disease=disease
        self.room_no=room_no
        
    def get_info(self):
        return f'''name:{self.name}
                   age:{self.age}
                   disease:{self.disease}
                   room_no:{self.room_no}'''
                   
    def __str__(self):
        return f'''name:{self.name}
                   age:{self.age}
                   disease:{self.disease}
                   room_no:{self.room_no}'''
                   
    def __lt__(self,other):
        return (self.age<other.age)
    
class Doctor(Person):
    def __init__(self,name,age,specialization,fee):
        super().__init__(name,age)
        self.specialization=specialization
        self.fee=fee
        
    def get_info(self):
        return f'''name:{self.name}
                   age:{self.age}
                   specialization:{self.specialization}
                   fee:{self.fee}'''              
        
class Hospital():
    def __init__(self,patient,doctor):
        self.patient.append(patient)
        self.doctor.append(doctor)
        
    def add_patient(self,patient):
        return self.Patient.append(patient)
   
    def add_doctor(self,doctor):
        return self.Doctor.append(doctor) 
    
    def show_patients(self):
        for i in self.Patient:
            print(i.get_info())
    
    def show_patients(self):
        for j in self.Doctor:
            print(j.get_info())
    
    def max_exp(self):
     return max(self.doctor, key=lambda d: d.fee)

    def young_patient(self):
     return min(self.patient, key=lambda p: p.age)
