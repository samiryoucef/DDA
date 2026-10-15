from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class HelloService(ServiceBase):

    @rpc(_returns=Unicode)
    def say_hello(ctx):
        return "Bonjour"


application = Application(
    [HelloService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)


if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Service SOAP démarré sur http://localhost:8000")
    server.serve_forever()
