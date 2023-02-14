class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


class Emp(person):
    def Print(self):
        print("Emp class called")


Emp_details = Emp("Mayank", 103)
Emp_details.display()
Emp_details.Print()