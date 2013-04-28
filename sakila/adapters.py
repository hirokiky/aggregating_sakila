from .utils import datetime_to_timestamp


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


    @property
    def first_of_x(self):
        try:
            return self.x[0]
        except IndexError:
            return None

    @property
    def first_of_x_as_timestamp(self):
        first_of_x = self.first_of_x
        if first_of_x:
            return datetime_to_timestamp(first_of_x)
        else:
            return None