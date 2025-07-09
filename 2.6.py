class Temperature:
    def __init__(self, celsius ):
        self.celsius = celsius

    @classmethod
    def creates_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def is_freezing(temperature):
        return temperature <= 0

temp = Temperature(25)
print(temp.kelvin)
