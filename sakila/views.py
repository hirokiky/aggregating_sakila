#! -*- coding:utf-8 -*-
from pyramid.view import view_config

from js.highcharts import highcharts

from .adapters import LinechartDataAdapter
from .charts import daily_linechart_options


@view_config(
    route_name='home',
    renderer='sakila:templates/home.mako')
def home(request):
    highcharts.need()

    adapter = LinechartDataAdapter(request.context.linechart)
    options = daily_linechart_options(adapter.x, adapter.y)

    return {'options': options}
