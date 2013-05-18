from highcharts import Chart
from highcharts.config_sections import ChartConfig, XAxisConfig
from highcharts.series import LineSeries

from .tochart import tochart_config
from .tochart.linechart import Linechart
from .utils import first_of, datetime_to_timestamp


def daily_linechart_options(x, y, renderTo='container'):
    series = LineSeries(data=y,
                        pointInterval=24 * 3600000,
                        pointStart=datetime_to_timestamp(first_of(x)))
    chart_config = ChartConfig(renderTo=renderTo)
    xaxis_config = XAxisConfig(type='datetime',
                               maxZoom=len(x) * 24 * 3600000)
    chart = Chart(chart=chart_config,
                  xAxis=xaxis_config)
    chart.add_series(series)

    return str(chart)


@tochart_config(name='')
def daily(request, data):
    return Linechart(data)
