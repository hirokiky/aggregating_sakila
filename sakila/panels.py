from pyramid.exceptions import NotFound
from pyramid_layout.panel import panel_config

from js.highcharts import highcharts

from .adapters import LinechartDataAdapter, PiechartDataAdapter
from .charts import daily_linechart_options, piechart_options


@panel_config(
    name='total_table',
    renderer='sakila:templates/panels/total_table.mako')
def total_table(context, request):
    try:
        table = context.summary
    except NotFound:
        table = None
    return {'total_table': table}


@panel_config(
    name='ranking_table',
    renderer='sakila:templates/panels/ranking_table.mako')
def ranking_table(context, request):
    try:
        ranking = context.ranking
    except NotFound:
        ranking = None
    return {'ranking_table': ranking}


@panel_config(
    name='linechart',
    renderer='sakila:templates/panels/linechart.mako')
def line_chart(context, request, renderTo='container'):
    highcharts.need()

    adapter = LinechartDataAdapter(request.context.linechart)
    options = daily_linechart_options(adapter.x, adapter.y,
                                      renderTo=renderTo)

    return {'options': options,
            'renderTo': renderTo}


@panel_config(
    name='piechart',
    renderer='sakila:templates/panels/piechart.mako')
def pie_chart(context, request, renderTo='container'):
    highcharts.need()

    adapter = PiechartDataAdapter(request.context.piechart)
    options = piechart_options(adapter.data,
                               renderTo=renderTo)
    return {'options': options,
            'renderTo': renderTo}
