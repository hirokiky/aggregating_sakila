from pyramid.exceptions import NotFound

import colander
from sqlalchemy import sql

from .models import (
    DBSession,
    Payment,
    Rental,
    Inventory,
    Film,
    Category,
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

        
        return (Payment.payment_date>=conditions['start_datetime']) &\
               (Payment.payment_date<conditions['end_datetime'])

    @property
    def summary(self):
        t = DBSession.query(
            sql.func.sum(Payment.amount),
            sql.func.count(Payment.payment_id),
            ).filter(self.conditions)
        return t

    @property
    def ranking(self):
        t = DBSession.query(
                Film.title,
                sql.func.sum(Payment.amount).label('sum_amount'),
                sql.func.count(Payment.payment_id).label('count_payment'),
                ).\
            join(Payment.rental).\
            join(Rental.inventory).\
            join(Inventory.film).\
            filter(self.conditions).group_by(Film.film_id).\
            order_by(sql.desc('sum_amount')).\
            order_by(sql.desc('count_payment')).limit(100)
        return t

    @property
    def linechart(self):
        c = DBSession.query(
                sql.func.date(Payment.payment_date).label('date'),
                sql.func.sum(Payment.amount),
                ).\
            filter(self.conditions).group_by('date')
        return c

    @property
    def piechart(self):
        c = DBSession.query(
                Category.name,
                sql.func.sum(Payment.amount).label('total_amount'),
                ).\
            join(Payment.rental).\
            join(Rental.inventory).\
            join(Inventory.film).\
            join(Film.category).\
            filter(self.conditions).group_by(Category.category_id).\
            order_by(sql.desc('total_amount'))
        return c
