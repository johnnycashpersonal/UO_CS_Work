class Employee:

    raise_amt = 1.04 # Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.'+ last + '@company.com' #this is an alternative way to do the same thing as above.
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10 # Class variable

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # This passes the first, last, and pay to the Employee class - the super class of Developer 
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
              self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
              self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Hunter', 'Schafer', 50000, 'python')
dev_2 = Developer('Jacob', 'Elordi', 60000, 'java')

mgr_1 = Manager('Becky', 'Moore', 100000, [dev_1, dev_2])
mgr_2 = Manager('kevin', 'Moore', 100000, [dev_2])

print(isinstance(mgr_1, Employee)) # True

#However, this wouldn't be true if we did the following:
print(isinstance(mgr_1, Developer)) # False

# This is because mgr_1 is an instance of the Manager class, which is a subclass of the Employee class. 
# Developer is also a subclass of the Employee class, but it is not a subclass of the Manager class.
