from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# Liste d'étudiants en mémoire
students = [
    {"id": 1, "name": "Youcef", "age": 21},
    {"id": 2, "name": "Samir", "age": 41},
]

# Définition d'un type complexe Student
class Student(ComplexModel):
    id = Integer
    name = Unicode
    age = Integer

class StudentService(ServiceBase):

    @rpc(_returns=Iterable(Student))
    def get_all_students(ctx):
        """
        Renvoie tous les étudiants de la liste
        """
        # Convertir le dictionnaire en Student
        return [Student(**s) for s in students]


# Création de l'application Spyne
application = Application(
    [StudentService],
    tns='spyne.examples.students',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Service SOAP démarré sur http://localhost:8000")
    server.serve_forever()
