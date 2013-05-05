class LinechartDataAdapter(object):
    def __init__(self, value):
        self.value = list(value)
        if self.value:
            self._x, self._y = tuple(zip(*self.value))
        else:
            self._x = self._y = []

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return [float(y) for y in self._y if y is not None]


class PiechartDataAdapter(object):
    def __init__(self, value):
        self.value = list(value)

    @property
    def data(self):
        return self.value