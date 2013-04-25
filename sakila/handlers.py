import decimal

def highcharts_linechart_handler(obj):
    if hasattr(obj, 'timetuple'):
        return 'Date.UTC(%s, %s, %s)' % obj.timetuple()[:3]
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return obj
