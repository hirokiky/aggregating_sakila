from zope.interface import implementer

from .interfaces import ILinechart

@implementer(ILinechart)
class Linechart(object):
    __used_for__ = list

    def __init__(self, context):
        self.context = context

    def getX(self):
        return [x for x, y in self.context]

    def getY(self):
        return [y for x, y in self.context]
