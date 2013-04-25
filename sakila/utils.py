# -*- coding:utf-8 -*-
import time

def utc_mktime(utc_tuple):
    """Returns number of seconds elapsed since epoch
    Note that no timezone are taken into consideration.
    utc tuple must be: (year, month, day, hour, minute, second)
    """

    if len(utc_tuple) == 6:
        utc_tuple += (0, 0, 0)
    return time.mktime(utc_tuple) - time.mktime((1970, 1, 1, 0, 0, 0, 0, 0, 0))


def datetime_to_timestamp(dt):
    """Converts a datetime object to UTC timestamp"""

    return int(utc_mktime(dt.timetuple()))
