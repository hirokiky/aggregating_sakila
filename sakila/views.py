#! -*- coding:utf-8 -*-
from pyramid.view import view_config

from highcharts import Chart
from highcharts.config_sections import ChartConfig, XAxisConfig
from highcharts.series import LineSeries
from js.highcharts import highcharts

from .adapters import LinechartDataAdapter


@view_config(
    route_name='home',
    renderer='sakila:templates/home.mako')
def home(request):
    highcharts.need()

    adapter = LinechartDataAdapter(request.context.linechart)

    series = LineSeries(data=adapter.y,
                        pointInterval=24*3600000,
                        pointStart=adapter.first_of_x_as_timestamp)
    chart_config = ChartConfig(renderTo='container')
    xaxis_config = XAxisConfig(type='datetime',
                               maxZoom=len(adapter.x) * 24 * 3600000)
    chart = Chart(chart=chart_config,
                  xAxis=xaxis_config)
    chart.add_series(series)

    return {'options': str(chart)}
