from abc import ABC, abstractmethod
class Lion(ABC):
    @abstractmethod
    def run(self):
        print('Бежать')

class Animal(Lion):
    def run(self):
        print('Бежать')

    def fly(self):
        print('Летать')

    def swim(self):
        print('Плавать')