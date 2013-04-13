from pyramid.exceptions import NotFound
from pyramid_layout.panel import panel_config


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
    name='line_chart',
    renderer='sakila:templates/panels/line_chart.mako')
def line_chart(context, request):
    chart = context.linechart
    return {'line_chart': chart}


@panel_config(
    name='pie_chart',
    renderer='sakila:templates/panels/pie_chart.mako')
def pie_chart(context, request):
    chart = context.piechart
    return {'pie_chart': chart}
