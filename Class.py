#amount
#category

class Budget:
    #amount = []

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

        #methods
    def deposit(self):
        return 'this is a deposit method'

    def check_balance(self):
        pass

    def withdrawal(self):
        pass
    def transfer(self):
        pass

category = Budget('Clothing', 1000)
category_1 = Budget('Food', 1000)
category_2= Budget('Entertainment', 1000)

#print(Budget(category_1))

class Car:
    #this defines the constructor
    def __init__(self, name, color):
        self.model = name
        self.color = color

    def my_car(self):
        print("My car's model is", self.model)

myCar1 = Car("BMW", "White")
myCar1.model = "Toyota"
#print(myCar1.my_car())


class MyClass:
    def __init__(self, height):
        self.height = 20

myHeight = MyClass(100)
del myHeight.height 
print(myHeight.height)

#class Person:
    #def __init__(self, fname, lname):
        #self.firstname = fname
        #self.lastname = lname
    #def printname(self):
        #print(self.firstname, self.lastname)
    #Here, we create the child
#class Student(Person):
    #pass

#Use the Person class to create an object, and then execute the printname method. 
#x = Person("John", "Doe")
#x.printname()

class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def printname(self):
        print(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, fname, lname, age, gender):
        super().__init__(fname, lname)
        self.age = age
        self.gender = gender

myStudent = Student("Mike", "Olsen", 29, 'male')

print(myStudent.age + ',' + myStudent.gender)



class Employee:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.last_name = lname
    
    def printname(self):
        print(self.firstname, self.last_name)

class Student1(Person):
    def __init__(self, fname, lname, age, gender):
        super().__init__(fname,lname)
        self.age = age
        self.gender = gender

    def student_profile(self):
        print("The student profile is listed below")
        print("Firstname-", self.first_name)
        print("Lastname-", self.last_name)
        print("Age-", self.age)

x = Student1("Mike", "Olsen", 24, "male")
x.student_profile()













