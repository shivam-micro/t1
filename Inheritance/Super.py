class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


class Emp(person):
    def __init__(self, name, id):
        super().__init__(name, id)

    def Print(self):
        print(self.name + " is an employee having id " + str(self.id))


Emp_details = Emp("Shivam", 103)
Emp_details.display()
Emp_details.Print()