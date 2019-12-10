from pyramid.view import view_config
from pyramid.config import Configurator
import logging


logging.basicConfig(level=logging.DEBUG)


def includeme(config):
    config.include('.kafka')
    config.add_route('app', '/')
    config.scan('.')


@view_config(route_name='app')
def app_route(request):
    request.response.status_int = 200
    return request.response


config = Configurator()
config.include(includeme)
application = config.make_wsgi_app()
