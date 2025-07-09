class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f'Имя: {self.name}, Позиция: {self.position}, Зарплата: {self.salary}'


class Developer(Employee):
    def __init__(self, name, salary, progrraming_language):
        super().__init__(name, 'Разработчик', progrraming_language)
        self.progrramig_language = progrraming_language

    def get_info(self):
        return f'{super().get_info()}, ЯП: {self.progrramig_language}'


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, 'Менеджер', salary)
        self.employes = []

    def add_empl(self, employe):
        self.employes.append(employe)

    def get_info(self):
        employee_names = ', '.join(emp.name for emp in   self.employes) if self.employes else "Нет подчинённых"
        return f"{super().get_info()}, Подчинённые: {employee_names}"

dev1 = Developer('Макс', 1500000,'Python' )
dev2 = Developer('Мария', 10000, 'Java')
manager = Manager('Леха', 140000)
manager.add_empl(dev1)
manager.add_empl(dev2)
print(manager.get_info())
