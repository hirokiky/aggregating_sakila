import copy


class AttributeSupplier(object):
    def __init__(self, *args):
        self.consts_module = __import__(*args)

    def __getattr__(self, name):
        return copy.deepcopy(getattr(self.consts_module, name))

consts = AttributeSupplier('constant_values', globals(), locals(), ['sakila', 'consts'])
