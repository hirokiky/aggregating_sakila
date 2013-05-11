from sqlalchemy import sql

from js.highcharts import highcharts
from pyramid.renderers import render
from zope.component import adapts, getGlobalSiteManager
from zope.interface import implements
from .charts import daily_linechart_options
from .interfaces import IRenderer, ILinechart, IResource
from .models import Payment


class HighchartsLinechartRenderer(object):
    implements(IRenderer)
    adapts(ILinechart)

    renderTo = 'container'

    def __init__(self, context):
        highcharts.need()

        self.context = context

        self.options = daily_linechart_options(
            self.context.getX(),
            self.context.getY(),
            renderTo=self.renderTo,
        )

    def render(self):
        result = render(
            'sakila:templates/renderer/highcharts/linechart.mako',
            {'options': self.options,
            'renderTo': self.renderTo})
        return result


class ResourceDailyLinechart(object):
    implements(ILinechart)
    adapts(IResource)

    def __init__(self, context):
        self.context = context
        self.points = self.context.resource.\
            add_column(sql.func.sum(Payment.amount)).\
            add_column(sql.func.date(Payment.payment_date).label('date')).\
            group_by('date').\
            all()

    def getX(self):
        return [x for y, x in self.points]

    def getY(self):
        return [y for y, x in self.points]


def set_adapters():
    gsm = getGlobalSiteManager()
    gsm.registerAdapter(ResourceDailyLinechart,
                        (IResource,), ILinechart, 'daily')
    gsm.registerAdapter(HighchartsLinechartRenderer,
                        (ILinechart,), IRenderer, 'highcharts')
