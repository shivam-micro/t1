
class Animal:
    def __init__(self):
        print('animal created')
    def speak(self):
        print('some animals are able to speak')
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
Felix = Cat( 'Felix')
for pet in [Niko, Felix]:
       print( pet.speak() )