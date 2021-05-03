class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay, ):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod 
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Timmy', "Harris", 350)
emp_2 = Employee('Sara', "Diaz", 600)

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))


#class_method example:
#emp_str_1 = 'John-Doe-700'
#emp_str_2 = 'Steve-Smith-3000'
#emp_str_3 = "Jane-Doe-9000"

#new_emp_1 = Employee.from_string(emp_str_1)

#print(new_emp_1.email)
#print(new_emp_1.pay)