class Employee:

    num_of_emps = 0 # Gets set to 0 as default, but gets incremented by 1 each time an Employee is created (with the += line below)
    raise_amount = 1.04 # This is a class variable to be shared among all instances of a class
    
    def __init__(self, first, last, pay):
        self.first = first # This is an instance variable for data unique to the class
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 # Increments by one each time a new employee is created

    def __repr__(self): # Magic/dunder method; unambiguous representation of object for debugging, etc.
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self): # Readable representation of an object; meant for display to end-user (falls back to __repr__ if __str__doesn't exist)
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @property # Property decorator; allow us to call this without having to use () in the call
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter # Setter that allows us to update first and last if fullname is updated
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter # Deleter that allows us to run cleanup code if an employee is deleted
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # raise_amount needs a reference to the class instance

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee): # This is a subclass of Employee and inherits all its attributes and methods
    raise_amt = 1.10 # Overrides the base Employee raise_amt

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Lets us inherit all the init code from Employee class without repeating code
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None): # Sets default list of employees that report to this manager to None
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
            print('-->', emp.fullname()) # Don't forget parenthesis


emp_1 = Employee('Corey', 'Schafer', 50000)

emp_1.fullname = 'Corey Schafer' # Only works because of the setter above

print(emp_1.first)
print(emp_1.email) # Works because of the @property decorator above
print(emp_1.fullname)

del emp_1.fullname # Only works with the deleter defined above

# print(len('test')) # Prints length of a string
# print('test'.__len__()) # Same as above, but explicitly calls __len__
# print(len(emp_1))

# print(emp_1 + emp_2)

# print(emp_1) # Calls __str__ by default

# print(repr(emp_1)) # Explicitly accessess __repr__
# print(str(emp_1)) # Explicitly accessess __str__

# print(1+2) # Calls __add__

# print(int.__add__(1,2)) # Explicitly calls __add__
# print(str.__add__('a','b'))

# print(help(Developer)) # Gives information about our Developer class!

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(isinstance(mgr_1, Manager)) # Is mgr_1 an instance of Manager?
# print(issubclass(Developer, Employee)) # Is Developer a subclass of Employee?