#! -*- coding:utf-8 -*-

from js.highcharts import highcharts
from pyramid_layout.panel import panel_config

from .interfaces import IHighchart


@panel_config(
    name='sidebar',
    renderer='sakila:templates/panels/sidebar.mako'
)
def sidebar(context, request):
    return dict(menus=[
        (u'速報', request.route_url('home')),
        (u'全体集計', None),
        (u'売上推移', '#'),
        (u'売上割合', '#'),
        (u'ランキング', '#'),
    ])


@panel_config(
    name='linechart',
    renderer='sakila:templates/panels/highcharts/linechart.mako'
)
def linechart(context, request, renderTo='container'):
    highcharts.need()

    reg = request.registry.getAdapter(request.context.linechart,
                                      IHighchart, '')
    options = reg.getOptions(renderTo=renderTo)

    return dict(options=options,
                renderTo=renderTo)
