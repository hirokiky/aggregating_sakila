def highcharts_linechart_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    return obj
