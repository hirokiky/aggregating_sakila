import decimal

from highcharts.encoders import ObjectEncoder


class SakilaEncoder(ObjectEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return super(SakilaEncoder, self).default(obj)
