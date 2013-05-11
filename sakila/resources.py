from pyramid.exceptions import NotFound

import colander
import zope.interface

from .interfaces import IResource
from .models import (
    DBSession,
    Payment,
    )
from .validators import ConditionSchema


class Resource(object):
    zope.interface.implements(IResource)

    def __init__(self, resource):
        self.resource = resource


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
    def resource(self):
        resource = DBSession.query().\
            filter(self.conditions)

        return Resource(resource)
