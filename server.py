from wsgiref.simple_server import make_server
from pyramid.view import view_config
from pyramid.config import Configurator
from pyramid.response import Response
from processor import executor
from json import loads

@view_config(route_name='process', renderer='json',
             request_method='POST')
def post(request):
    results=executor.addOperation(loads(request.body,
                                       encoding=request.charset))
    request.response.status = results['code']
    return results

@view_config(route_name='info', renderer='json',
             request_method='GET')
def get(request):
    results=executor.getservices(request.matchdict['service'])
    return results

@view_config(route_name='results', renderer='json',
             request_method='GET')
def results(request):
    result=executor.getstatus(request.matchdict['idreq'])
    request.response.status=result['code']
    return result

def pregenservices(request, elements, kw):
    kw.setdefault('service', '')
    return elements, kw

def start_server():
    config = Configurator()
    config.add_route('process', '/service')
    config.add_route('info', '/info/{service:.*}',pregenerator=pregenservices)
    config.add_route('results', '/results/{idreq}')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print(server.base_environ)
    server.serve_forever()


if __name__ == '__main__':
    start_server()
