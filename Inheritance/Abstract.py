from abc import ABC, abstractmethod
class Animal(ABC):
        def speak(self):
            pass
class Dog(Animal):
        def __init__(self, name):
            self.name = name
        def speak(self):
           return self.name + ' says woof '
class Cat(Animal):
        def __init__(self, name):
            self.name = name
        def speak(self):
            return self.name + ' says meow '
Niko = Dog('Niko')
print(Niko.speak())
Felix = Cat('Felix')
print(Felix.speak())