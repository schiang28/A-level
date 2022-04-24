class Employee:

    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.pay = pay
        # self.email = first + "." + last + "@company.com"

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    """def apply_raise(
        self,
    ):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
    """


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
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
            print("-->", emp.fullname())


emp_1 = Employee("John", "Smith")

emp_1.fullname = "Corey Shafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
