import zope.interface


class IRenderer(zope.interface.Interface):
    def render():
        """ Providing as HTML """


class ILinechart(zope.interface.Interface):
    def getX():
        """ Providing points of x axis """

    def getY():
        """ Providing points of y axis. """


class IResource(zope.interface.Interface):
    resource = zope.interface.Attribute('Basic resource for all aggregations.')
    conditions = zope.interface.Attribute('Condition for getting a resource.')
