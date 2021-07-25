class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Для творчества вы используете {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'На столе лежит {self.title}. Вы её взяли и сделали красивый набросок.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title} для своего будущего чертежа'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}, чтобы подчеркнуть важные моменты в своём конспекте'


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
