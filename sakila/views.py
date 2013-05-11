#! -*- coding:utf-8 -*-
from pyramid.view import view_config
from zope.component import getAdapter

from .interfaces import ILinechart, IRenderer


@view_config(
    route_name='home',
    renderer='sakila:templates/home.mako')
def home(request):
    linechart = getAdapter(request.context.resource,
                           ILinechart, 'daily')
    renderer = getAdapter(linechart,
                          IRenderer, 'highcharts')
    return {'renderer': renderer}
