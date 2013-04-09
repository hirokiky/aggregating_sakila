from pyramid.view import view_config

@view_config(
    route_name='home',
    renderer='sakila:templates/home.mako')
def home(request):
    return {}
