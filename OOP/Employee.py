class Emp:

    def __init__(self,name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee(self):
        print(self.name, self.age, self.salary)


Emp_details = Emp("Mayank", 10, 10000)
Emp_details.display_employee()
