from js.highcharts import highcharts

from highcharts import Chart
from highcharts.config_sections import ChartConfig, XAxisConfig
from highcharts.series import LineSeries
from zope.interface import implementer

from .interfaces import ILinechart
from .utils import datetime_to_timestamp, first_of


@implementer(ILinechart)
class Linechart(object):
    __used_for__ = list

    def __init__(self, context):
        self.context = context

    def getX(self):
        return [x for x, y in self.context]

    def getY(self):
        return [y for x, y in self.context]

    @property
    def highchartable(self,
                      renderTo='container',
                      pointInterval=24 * 3600000):
        highcharts.need()

        series = LineSeries(data=self.getY(),
                            pointInterval=pointInterval,
                            pointStart=datetime_to_timestamp(first_of(self.getX())))
        chart_config = ChartConfig(renderTo=renderTo)
        xaxis_config = XAxisConfig(type='datetime',
                                   maxZoom=len(self.context) * pointInterval)
        chart = Chart(chart=chart_config,
                      xAxis=xaxis_config)
        chart.add_series(series)

        return str(chart)