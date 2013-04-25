#! -*- coding:utf-8 -*-
import json

from pyramid.view import view_config

from .adapters import LinechartDataAdapter
from .consts import consts
from .handlers import highcharts_linechart_handler
from .utils import datetime_to_timestamp


@view_config(
    route_name='home',
    renderer='sakila:templates/home.mako')
def home(request):
    adapter = LinechartDataAdapter(request.context.linechart)
    options = consts.HIGHCHARTS_OPTIONS_BASE

    first_of_x = adapter.first_of_x
    first_of_x = datetime_to_timestamp(first_of_x) if first_of_x else None

    options['chart']['renderTo'] = 'container'
    options['xAxis']['type'] = 'datetime'
    options['xAxis']['maxZoom'] = '24 * 3600000'
    options['series'] = [{'name': 'test',
                          'pointInterval': 24 * 3600 * 1000,
                          'pointStart': first_of_x,
                          'data': adapter.y}]
    options = json.dumps(options, default=highcharts_linechart_handler)

    return {'options': options}
