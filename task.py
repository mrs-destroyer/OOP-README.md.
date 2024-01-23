from datetime import date

# Class, Object and Members
class A:
    name = "Asad"
    age = 25
    def func(self):
        name = "Ahmad"
        print(name)
obj = A()
obj.func()
print(obj.name) 
print(A.age)


 
# Data Hiding and Object Printing
# Encapsulation
class A:
    __a = 6 # private
    _b = 4 
    def Show(self):
        print("a = " , self.__a)
        print("b = " , self._b)
obj= A()
obj.Show()
#print("Outside the class " , obj.__a) 
print("Outside of class " , obj._b) 



# Inheritance in Python
class Parents:
    def Lands(self):
        print("Having their own properties")
class Child(Parents):
    def Money(self):
        print("Access parents property")

C = Child()
C.Lands()
C.Money()     

#issubclass
class Building:
    pass
class School(Building):
    pass
class Schoolstudents(School):
    pass

print(issubclass(School,(Building)))
print(issubclass(Building,(Schoolstudents)))
print(issubclass(Schoolstudents,Building))
print(issubclass(Building,Building))  

#superclass
class Computer(object):
    def __init__(self):
        self.ram = "8gb"
        self.storage = "512gb"
        print("Computer class constructor is " )
class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.model = "iphone X"
        print("Mobile class constructor is  ")

Apple = Mobile()
print(Apple.__dict__)        



# Polymorphism in Python
print("Asad")
print(6+4)
print(len("Asad"))
print(len(["Asad" , "Ahmad"]))


# Class method and static method in python
#Staticmethod
class Calculator:
    def __init__(self, version: int):
        self.version = version
    def description(self):
        print(f"Running calculator in version : {self.version}")
    @staticmethod
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)
if __name__ == '__main__':
    calc1 = Calculator (10)
    calc2 = Calculator (200)
    calc1.description()
    calc2.description()
    print(Calculator.add_numbers(10,20))

#Class Method 
class Person:
    def __init__ (self , name: str, age: int):
        self.name = name
        self.age = age 
    def description(self) -> str:
        return f"{self.name} is {self.age} years old. "
    @classmethod 
    def age_from_year(cls, name: str, birth_year: int): 
        current_year: int = date.today().year 
        age: int = current_year - birth_year
        return cls(name,age) 
if __name__ == "__main__":
    Asad = Person.age_from_year("Asad" , 1999)
    print(Asad.description()) 
