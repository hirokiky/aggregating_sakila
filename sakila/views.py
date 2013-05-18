#! -*- coding:utf-8 -*-
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import notfound_view_config, view_config


@notfound_view_config(append_slash=True)
def notfound(request):
    return HTTPNotFound('Not found, bro.')


@view_config(
    route_name='home',
    renderer='sakila:templates/home.mako')
def home(request):
    return {}
