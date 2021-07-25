from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def __init__(self):
        self.color_1 = TrafficLight.__color[0]
        self.color_2 = TrafficLight.__color[1]
        self.color_3 = TrafficLight.__color[2]

    def running(self):
        print(f'{self.color_1} цвет - проезда нет')
        sleep(7)
        print(f'{self.color_2} цвет - будь готов к пути')
        sleep(2)
        print(f'А {self.color_3} цвет - кати!')
        sleep(1)
        TrafficLight.repeat(self)

    def repeat(self):
        try:
            ans = int(input('Повторить стих? (1 - Да, 0 - Нет): '))
            if ans == 1:
                return TrafficLight.running(self)
            elif ans != 1 and ans != 0:
                print('Введите 1 или 2')
                return TrafficLight.repeat(self)
            else:
                print('До встречи :^)')
        except ValueError:
            print('Введите 1 или 2')
            return TrafficLight.repeat(self)


Svetophor = TrafficLight()
Svetophor.running()
