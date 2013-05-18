import datetime

import venusian

from .interfaces import ILinechart


def tochart_config(name='', chart_type='linechart'):
    def dec(callable):
        def callback(scanner, _name, ob):
            scanner.config.set_tochart(callable, name, chart_type)
        venusian.attach(callable, callback)
        return callable
    return dec


def set_tochart(config, callable, name="", chart_type='linechart'):
    type = ILinechart
    callable = config.maybe_dotted(callable)
    reg = config.registry

    def register():
        reg.registerAdapter(callable,
                            [datetime.datetime, datetime.datetime],
                            #TODO chart_type -> own Interface.
                            ILinechart,
                            name=name)
    intr = config.introspectable(category_name='tochart',
                                 discriminator='tochart of {0}'.format(type.__name__),
                                 title='tochart of {0}'.format(type.__name__),
                                 type_name=None)
    config.action('tochart', register,
                  introspectables=(intr,))


def tochart(request, value, name=''):
    adapted = request.registry.getMultiAdapter([request, value],
                                               ILinechart,
                                               name=name)
    return adapted
