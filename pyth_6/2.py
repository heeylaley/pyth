class Road:
    def __init__(self, _length, _width, _depth):
        self._length = _length
        self._width = _width
        self._depth = _depth

    def calc_asphalt(self):
        return f'Масса асфальта для покрытия дороги = {self._length * self._width * self._depth * 25} т.'


this_road = Road(100, 10, 10)
print(this_road.calc_asphalt())
