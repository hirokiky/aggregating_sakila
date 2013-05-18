from sqlalchemy import sql

from .models import (
    DBSession,
    Payment,
    )
from .tochart import tochart_config


@tochart_config(name='daily.linechart',
                chart_type='linechart')
def daily(request, data):
    start_datetime, end_datetime = request.context.period

    condition = ((Payment.payment_date >= start_datetime) &
                 (Payment.payment_date < end_datetime))
    return DBSession.query(
        sql.func.date(Payment.payment_date).label('date'),
        sql.func.sum(Payment.amount),
    ).group_by(
        'date'
    ).filter(condition).all()
