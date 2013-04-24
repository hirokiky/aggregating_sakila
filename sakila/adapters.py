import json

from .handlers import highcharts_linechart_handler


class LinechartDataAdapter(object):
    def __init__(self, value):
        self.value = value
        self.series, self.categories = tuple(zip(*value))

    @property
    def highcharts_json_series(self):
        json_series = json.dumps(self.series,
                                 default=highcharts_linechart_handler)
        return json_series

    @property
    def highcharts_json_categories(self):
        json_categories = json.dumps(self.categories,
                                     default=highcharts_linechart_handler)
        return json_categories
