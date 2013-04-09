import datetime

import colander


@colander.deferred
def deferred_start_datetime_missing(node, kw):
    default_datetime = kw.get('default_datetime')
    if default_datetime is None:
        default_datetime = datetime.datetime.now()
    return default_datetime


@colander.deferred
def deferred_end_datetime_missing(node, kw):
    default_datetime = kw.get('default_datetime')
    if default_datetime is None:
        default_datetime = datetime.datetime.now() + datetime.timedelta(days=1)
    return default_datetime


class ConditionSchema(colander.MappingSchema):
    start_datetime = colander.SchemaNode(
        colander.DateTime(),
        missing=deferred_start_datetime_missing)
    end_datetime = colander.SchemaNode(
        colander.DateTime(),
        missing=deferred_end_datetime_missing)

