class Person:

    def __init__(self):
        self.name = "Jalen"
        self.age = 28
    
    #Create a function that changes the age
    def update(self):
        self.age = 30

first_person = Person()
second_person = Person()

#change first_person name
first_person.name = 'Harris'

print(first_person.name)
print(second_person.age)

first_person.update()
