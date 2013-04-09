from sqlalchemy import sql

from sakila.models import (
    DBSession,
    Payment,
    Rental,
    Inventory,
    Film,
    Category,
    )


def get_total(conditions):
    t = DBSession.query(
        sql.func.sum(Payment.amount),
        sql.func.count(Payment.payment_id),
        ).filter(conditions)
    return t


def get_ranking(conditions):
    t = DBSession.query(
            Film.title,
            sql.func.sum(Payment.amount).label('total_amount'),
            sql.func.count(Payment.payment_id),
            ).\
        join(Payment.rental).\
        join(Rental.inventory).\
        join(Inventory.film).\
        filter(conditions).group_by(Film.film_id).\
        order_by(sql.desc('total_amount')).limit(100)
    return t


def get_line(conditions):
    c = DBSession.query(
            sql.func.date(Payment.payment_date).label('date'),
            sql.func.sum(Payment.amount),
            ).\
        filter(conditions).group_by('date')
    return c


def get_pie(conditions):
    c = DBSession.query(
            Category.name,
            sql.func.sum(Payment.amount).label('total_amount'),
            ).\
        join(Payment.rental).\
        join(Rental.inventory).\
        join(Inventory.film).\
        join(Film.category).\
        filter(conditions).group_by(Category.category_id).\
        order_by(sql.desc('total_amount'))
    return c
