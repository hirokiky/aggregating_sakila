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
        except colander.Invalid:
            raise NotFound

        return conditions['start_datetime'], conditions['end_datetime']
