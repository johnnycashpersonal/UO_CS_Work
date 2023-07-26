class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.'+ last + '@company.com' #this is an alternative way to do the same thing as above.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Hunter', 'Schafer')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

