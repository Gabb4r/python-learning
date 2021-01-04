"""

class Phone:
    def __init__(self, height, display, camera, version):
        self.height = height
        self.display = display
        self.camera = camera
        self.version = version

oppo = Phone(6, 5.7, 13, 7)

vivo = Phone(5.5, 5.8, 20, 8)

print(f"This is vivo display =>",vivo.display)

print(f"this is my oppo camera {oppo.camera} mp lense")

"""

"""
class ok:
    name = "lol"
    def __init__(self):
        self.name= "GabbAr"
        

a = ok()

print(a.name)
print(ok.name)

"""

"""

class hero:
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

    def compare_power(self, other):         # to compare two diffrent objects
        if self.power == other.power:
            return True
        else:
            return False

ironman = hero('ironman', 35, 99)

captain = hero('captain', 28, 85)

if captain.compare_power(ironman):
    print("Both have same power")
else:
    print("Both have diffrent power")

"""

"""
class Student:
    school = ("S.T. Xaviers High School")        # class variable

    def __init__(self, maths, english, gujrati):    # instance variable
        self.maths = maths
        self.english = english
        self.gujrati = gujrati
    
    def set_marks_maths(self, marks):
        self.maths = marks

    def get_marks_maths(self):
        print(self.maths)
    
    def set_marks_english(self, marks):
        self.english = marks

    def get_marks_english(self):
        print(self.english)
    
    def set_marks_gujrati(self, marks):
        self.gujrati = marks

    def get_marks_gujrati(self):
        print(self.gujrati)
    
    def info(cls):     # this is example of class method
        print(Student.school)

    def ok():       # This is example of static method
        print("yes okay")

raj = Student(85, 45, 56)

raj.get_marks_gujrati()

raj.set_marks_gujrati(58)

raj.get_marks_gujrati()

raj.info()          # to call class method

Student.ok()        # to call static mathod

"""

'''

class A:
    def f1(self):
        print("f1 is working")
    def f2(self):
        print("f2 is working")

class B(A):             # Example of inheritance
    def f3(self):
        print("f3 is working")
    def f4(self):
        print("f4 is working")

a = A()
b = B()
b.f1()                     # Example of inheritance

'''

'''
class A:
    def f1(self):
        print("f1 is working")
    def f2(self):
        print("f2 is working")

class B(A):             
    def f3(self):
        print("f3 is working")
    def f4(self):
        print("f4 is working")

class C(B):             # multi lvl inheritance bcs class c taking all features from class a and class b 
    def f5(self):
        print("f5 is working")

a = A()
b = B()
c = C()

c.f1()                  # Multi lvl inheritance
'''
'''
class A:
    def f1(self):
        print("f1 is working")
    def f2(self):
        print("f2 is working")

class B:             
    def f3(self):
        print("f3 is working")
    def f4(self):
        print("f4 is working")

class C(A,B):               # Multiple inheritance
    def f5(self):
        print("f5 is working")


a = A()
b = B()
c = C()

c.f1()

'''

class A:

    def __init__(self):
        print("A is initiated")
    def f1(self):
        print("f1 is working")
    def f2(self):
        print("f2 is working")

class B:            

    def __init__(self):
        print("B is initiated")
    def f3(self):
        print("f3 is working")
    def f4(self):
        print("f4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()      # we can use super() method to tell to excute from super classes but remember if class has multiple classes than it will select from left to right , it's call Method Resolution Order (MRO)
        print("C is inititated")

a = C()           # so in this case , it will first look for in own class even if it's inheritance the other classes but if it's found same method in own class , it will excute it first for example here __init__ method


