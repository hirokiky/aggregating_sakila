import datetime

from pyramid.exceptions import NotFound

import colander

from .validators import ConditionSchema


class SakilaResource(object):
    def __init__(self, request):
        self.request = request

    @property
    def period(self):
        s = ConditionSchema().bind()


        try:
            conditions = s.deserialize(self.request.GET)
            start_datetime = conditions['start_datetime']
            end_datetime = conditions['end_datetime']
        except colander.Invalid:
            end_datetime = datetime.datetime.now()
            start_datetime = end_datetime - datetime.timedelta(days=7)

        return start_datetime, end_datetime
