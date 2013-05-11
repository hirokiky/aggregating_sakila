#! -*- coding:utf-8 -*-

from pyramid_layout.panel import panel_config


@panel_config(
    name='sidebar',
    renderer='sakila:templates/panels/sidebar.mako'
)
def sidebar(context, request):
    return dict(menus=[
        (u'速報', request.route_url('home')),
        (u'全体集計', None),
        (u'売上推移', '#'),
        (u'売上割合', '#'),
        (u'ランキング', '#'),
    ])
