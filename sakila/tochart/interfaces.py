from zope.interface import Interface


class ILinechart(Interface):
    def getX():
        """ Points of x axis """

    def getY():
        """ Points of y axis """
