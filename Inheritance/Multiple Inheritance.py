class Base1():
    def __init__(self):
        self.str1 = 'Hello1'
        print("Base1")


class Base2():
    def __init__(self):
        self.str2 = 'Hello2'
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
