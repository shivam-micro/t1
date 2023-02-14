class Car:

    def __init__(self,model, year, make):
        self.model = model
        self.year = year
        self.make = make

    def display_car(self):
        print(self.model, self.year, self.make)


Emp_details = Car("Q7", 2025, "BMW")
Emp_details.display_car()
