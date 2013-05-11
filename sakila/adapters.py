from highcharts import Chart
from highcharts.config_sections import ChartConfig, XAxisConfig
from highcharts.series import LineSeries
from js.highcharts import highcharts
from zope.interface import implementer

from .interfaces import IHighchart, ILinechart
from .utils import first_of, datetime_to_timestamp


@implementer(IHighchart)
class LinechartHighcharts(object):
    __used_for__ = ILinechart

    def __init__(self, context):
        highcharts.need()
        self.context = context

    def getOptions(self, renderTo='container'):
        series = LineSeries(data=self.context.getY(),
                            pointInterval=24 * 3600000,
                            pointStart=datetime_to_timestamp(first_of(self.context.getX())))
        chart_config = ChartConfig(renderTo=renderTo)
        xaxis_config = XAxisConfig(type='datetime',
        maxZoom=len(self.context.getX()) * 24 * 3600000)
        chart = Chart(chart=chart_config,
                      xAxis=xaxis_config)
        chart.add_series(series)

        return str(chart)


@implementer(ILinechart)
class ListLinechart(object):
    def __init__(self, context):
        self.context = context

    def getX(self):
        return [x for y, x in self.context]

    def getY(self):
        return [y for y, x in self.context]
