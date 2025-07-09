from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Car(Transport):

    def start_engine(self):
        return 'Двигатель запущен'


    def stop_engine(self):
        return 'Двигатель остановлен'


    def move(self):
        return 'Машина двигается'

class Boat(Transport):

    def start_engine(self):
        return 'Двигатель запущен'


    def stop_engine(self):
        return 'Двигатель остановлен'

    def move(self):
        return 'Лодка двигается'



