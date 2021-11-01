class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} = {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name} выше дозволенной! ({self.speed} км/ч)'
        else:
            return f'Скорость {self.name} = {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name} выше дозволенной! ({self.speed} км/ч)'
        else:
            return f'Скорость {self.name} = {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bmw = SportCar(120, 'чёрная', 'bmw', False)
print(bmw.go())
print(bmw.stop())
print(bmw.turn_left())
print(bmw.show_speed())

mazda = TownCar(35, 'голубая', 'mazda', False)
print(mazda.go())
print(mazda.stop())
print(mazda.turn_right())
print(mazda.show_speed())

volvo = WorkCar(62, 'чёрная', 'volvo', True)
print(volvo.go())
print(volvo.stop())
print(volvo.turn_left())
print(volvo.show_speed())

chevrolet = PoliceCar(100, 'белая',  'chevrolet', True)
print(chevrolet.go())
print(chevrolet.stop())
print(chevrolet.turn_right())
print(chevrolet.show_speed())
