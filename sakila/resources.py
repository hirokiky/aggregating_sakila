from pyramid.exceptions import NotFound

import colander

from .models import Payment
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
