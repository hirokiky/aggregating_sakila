class LinechartDataAdapter(object):
    def __init__(self, value):
        self.value = list(value)
        if self.value:
            self.x, self.y = tuple(zip(*self.value))
        else:
            self.x = self.y = []

    @property
    def first_of_x(self):
        try:
            return self.x[0]
        except IndexError:
            return None

