from pyramid_layout.layout import layout_config

from js.bootstrap import bootstrap


@layout_config(template="sakila:templates/layouts/base.mako")
class BaseLayout(object):
    def __init__(self, config, request):
        self.config = config
        self.request = request

        bootstrap.need()
