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

    # This is a special method that allows us to change the way that the object is printed.
    # If we didn't have this method, we would get something like this:
    # <__main__.Employee object at 0x0000020F4F6F4E80>
    # But with this method, we can change it to something more readable.
    def __repr__(self): #this is for developers
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # This is a special method that allows us to change the way that the object is printed.
    # If we didn't have this method, we would get something like this:
    # <__main__.Employee object at 0x0000020F4F6F4E80>
    # But with this method, we can change it to something more readable.
    def __str__(self): #this is for end users
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Hunter', 'Schafer', 50000)
emp_2 = Employee('Jacob', 'Elordi', 60000)

# print(repr(emp_1))
# print(str(emp_1))

# These two lines of code do the same thing as the two lines above.
print(emp_1.__repr__())
print(emp_1.__str__())

print(len(emp_1))






