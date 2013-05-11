import zope.interface


class IHighchart(zope.interface.Interface):
    def getOptions(renderTo='container'):
        """ Providing a options """


class ILinechart(zope.interface.Interface):
    def getX():
        """ Points of x axis """

    def getY():
        """ Points of y axis """
