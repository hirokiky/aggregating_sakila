from js.highcharts import highcharts
from zope.interface import implementer

from .charts import daily_linechart_options
from .interfaces import IHighchart, ILinechart


@implementer(IHighchart)
class LinechartHighcharts(object):
    __used_for__ = ILinechart

    def __init__(self, context):
        highcharts.need()
        self.context = context

    def getOptions(self, renderTo='container'):
        chart = daily_linechart_options(self.context.getX(),
                                        self.context.getY(),
                                        renderTo=renderTo)

        return str(chart)


@implementer(ILinechart)
class ListLinechart(object):
    def __init__(self, context):
        self.context = context

    def getX(self):
        return [x for y, x in self.context]

    def getY(self):
        return [y for y, x in self.context]
