from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def spek(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def spek(self):
        return 'Woof'

    def move(self):
        return 'бегает'

class Bird(Animal):
    def spek(self):
        return 'Tweet!'

    def move(self):
        return "I'm flying!"
class Fish(Animal):
    def spek(self):
        return '...'

    def move(self):
        return "I'm swimming!"


def an(animal):
    print(animal.spek(), animal.move())

animals = [ Dog(), Bird(), Fish()]
for animal in animals:
    an(animal)


