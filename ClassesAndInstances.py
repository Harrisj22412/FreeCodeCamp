class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

emp_1 = Employee('James', 'Smith', 600)
emp_2 = Employee('Corey', 'Smith', 200)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

Employee.fullname(emp_1)

#emp_1.first = 'James'
#emp_1.last = "Smith"
#emp_1.pay = 600
#emp_1.email = 'James.smith@yahoo.com'

#emp_2.first = 'Corey'
#emp_2.last = "Smith"
#emp_2.pay = 200
#emp_2.email = 'Corey.smith@yahoo.com'

