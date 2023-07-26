# The basics of creating and Instantiating simple classes in python

class Employee:

    num_of_emps = 0 # Class variable
    raise_amount = 1.06 # Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.num_of_emps += 1 
        #this will add 1 to the num_of_emps class variable every time a new instance of the class is created, 
        #not just when the __init__ method is called.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #this will allow us to change the raise_amount for each instance of the class if we wanted to.

    @classmethod #this is a decorator, which alternates the functionality of the method below.
    def set_raise_amt(cls, amount): #cls is a convention for class.
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str): #this is an alternative constructor.
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #this will create a new instance of the class using the string above.

    @staticmethod #this is a decorator, which alternates the functionality of the method below.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: #this will check if the day is a weekend - 5 is saturday, 6 is sunday.
            return False
        return True

emp_1 = Employee('Hunter', 'Schafer', 50000)
emp_2 = Employee('Jacob', 'Elordi', 60000)

import datetime
my_date = datetime.date(2020, 7, 10)

print(Employee.is_workday(my_date)) #this will print True because it is a weekday.