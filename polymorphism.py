#Polymorphism
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

class cow:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am a cow.my name is{self.name}.I am {self.age} years old.")

    def make_sound(self):
        print("mmaaa") 



cat1 = cat("Kitty", 2)
dog1 = Dog("Fluffy", 4)
cow1=cow("pinkyy",4)
for animal in (cat1, dog1,cow1):
    animal.make_sound()
    animal.info()



'''class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"am a student.my name is {self.name}.am {self.age} years old")
    def info(self):
        print("marks")
class staff():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"am a staff.my name is {self.name}.am {self.age} years old")
    def info(self):
        print("marks")
obj1=student("arsha",24)
obj2=staff("krish",40)
obj1.details()
obj1.info()
obj2.details()
obj2.info()'''

#example
'''class employee():
    def __init__(self,employeename,salary,qualification):
        self.employeename=employeename
        self.salary=salary
        self.qualification=qualification
    def details(self):
        print(f"am a employee{self.employeename},{self.salary},{self.qualification}")
class hr():
    def __init__(self,employeename,salary,qualification):
        self.employeename=employeename
        self.salary=salary
        self.qualification=qualification
    def details(self):
        print(f"am a employee{self.employeename},{self.salary},{self.qualification}")
obj=employee("bhavya",23455,"b.sc")
obj2=hr("abi",23145,"m.sc")
obj.details()
obj2.details()'''

# #super function
#It is used to direct use child class parameters without parent class
'''class parent():
    def fun(self):
        print("they are aprent of arshi:")
class child(parent):
    def fun1(self):
        super().fun()
        print("theya re the best parent")
obj=child()
obj.fun1()'''

