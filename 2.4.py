from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def go(self):
        pass

class Sparrow(Bird):
    def go(self):
        print('ходит')

    def fly(self):
        print('Летает')

class Penguin(Bird):
    def go(self):
        print('ходит')

    def swimming(self):
        print('плавает в океане ')






