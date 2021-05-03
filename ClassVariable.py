class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@hotmail.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)


emp_1 = Employee("Corey", "Schafer", 5000)
emp_2 = Employee('Test', 'User', 600)


print(Employee.num_of_emps)
#print(Employee.__dict__)

#Employee.raise_amount = 1.5
#emp_1.raise_amount = 1.5
#print(emp_1.__dict__)

#print(emp_1.raise_amount)
#print(Employee.raise_amount)
#emp_1.apply_raise()
#print(emp_2.raise_amount)

