class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Работник: {self.name} {self.surname}'

    def get_full_income(self):
        return f'Доход с учётом премии = {self._income.get("wage") + self._income.get("bonus")} рублей'


pos = Position('Саша', 'Иванова', 'уборщик', 100000, 120000)
print(pos.get_full_name())
print(pos.get_full_income())
