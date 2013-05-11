from pyramid.exceptions import NotFound

import colander
from sqlalchemy import sql

from .adapters import ListLinechart
from .models import (
    DBSession,
    Payment,
    )
from .validators import ConditionSchema


class SakilaResource(object):
    def __init__(self, request):
        self.request = request

    @property
    def conditions(self):
        s = ConditionSchema().bind()

        try:
            conditions = s.deserialize(self.request.GET)
        except colander.Invalid:
            raise NotFound

        return (Payment.payment_date >= conditions['start_datetime']) &\
               (Payment.payment_date < conditions['end_datetime'])

    @property
    def linechart(self):
        resource = DBSession.query().\
            add_column(sql.func.sum(Payment.amount)).\
            add_column(sql.func.date(Payment.payment_date).label('date')).\
            group_by('date').\
            filter(self.conditions).\
            all()
        return ListLinechart(resource)
