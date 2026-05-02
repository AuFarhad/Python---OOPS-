from abc import ABC,abstractmethod

class Travel(ABC):
    def __init__(self,name,distance,duration):
        self.name=name
        self.distance=distance
        self.duration=duration
        
    @abstractmethod
    def get_info(self):
        pass
    
    
class Car(Travel):
    def __init__(self,name,distance,duration,seat):
        super().__init__(name,distance,duration)
        self.seat=seat

    def get_info(self):
        return f'''Name:{self.name}
                   distance:{self.distance}
                   duration:{self.duration}
                   seat:{self.seat}
                   '''
                   
    def __str__(self):
        return f'''Name:{self.name}
                   distance:{self.distance}
                   duration:{self.duration}
                   seat:{self.seat}
                   '''
    def __add__(self, other):
        return self.duration + other.duration
    
class Bus(Travel):
    def __init__(self,name,distance,duration,size):
        super().__init__(name,distance,duration)
        self.size=size
    
    def get_info(self):
        return f'''Name:{self.name}
                   distance:{self.distance}
                   duration:{self.duration}
                   size:{self.size}
                   '''
    def __str__(self):
        return self.get_info()


class Travelling():
    def __init__(self):
        self.travels=[]
        
    def add_travel(self,travel):
        self.travels.append(travel)
        
    def show_all(self):
        for travel in self.travels:
            print(travel.get_info()) 
        
    def max_value(self):
        return max(self.travels ,key= lambda d:d.duration)
    
    def min_value(self):
        return min(self.travels ,key= lambda d:d.duration)
    
c1=Car("Activa",100,4,7)
c2=Car("Honda",200,5,5)
c3=Car("TATA",300,4,8)
b1=Bus("Volvo",200,5,6)
b2=Bus("vest",100,7,9)
b3=Bus("shit",200,9,10)

Travels=Travelling()
Travels.add_travel(c1)
Travels.add_travel(c1)
Travels.add_travel(c1)
Travels.add_travel(b1)
Travels.add_travel(b2)
Travels.add_travel(b3)
 
Travels.show_all()
print("MAX duration :",Travels.max_value())
print("MIN duration :",Travels.min_value())


