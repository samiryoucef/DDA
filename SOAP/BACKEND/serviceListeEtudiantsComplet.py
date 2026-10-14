
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel, Fault
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


# Définition du service SOAP
class StudentService(ServiceBase):

    @rpc(_returns=Iterable(Student))
    def get_all_students(ctx):
        """
        Renvoie tous les étudiants de la liste
        """
        return [Student(**s) for s in students]

    @rpc(Integer, _returns=Student)
    def get_student_by_id(ctx, student_id):
        """
        Retourne un étudiant selon son ID
        """
        for s in students:
            if s["id"] == student_id:
                return Student(**s)

        return None  # Si l'étudiant n'est pas trouvé

    @rpc(Integer, Unicode, Integer, _returns=Student)
    def add_student(ctx, student_id, name, age):
        """
        Ajoute un nouvel étudiant
        """
        # Vérifier si l'ID existe déjà
        for s in students:
            if s["id"] == student_id:
                raise Fault(
                    faultcode='Client',
                    faultstring='ID déjà existant'
                )

        new_student = {
            "id": student_id,
            "name": name,
            "age": age
        }

        students.append(new_student)

        return Student(**new_student)

    @rpc(Integer, _returns=Unicode)
    def delete_student(ctx, student_id):
        """
        Supprime un étudiant selon son ID
        """
        for s in students:
            if s["id"] == student_id:
                students.remove(s)
                return f"Étudiant avec ID {student_id} supprimé avec succès"

        raise Fault(
            faultcode='Client',
            faultstring='Étudiant non trouvé'
        )

    @rpc(Integer, Unicode, Integer, _returns=Student)
    def update_student(ctx, student_id, name, age):
        """
        Modifie les informations d'un étudiant selon son ID
        """
        for s in students:
            if s["id"] == student_id:
                s["name"] = name
                s["age"] = age
                return Student(**s)

        raise Fault(
            faultcode='Client',
            faultstring='Étudiant non trouvé'
        )


# Création de l'application Spyne
application = Application(
    [StudentService],
    tns='spyne.examples.students',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)


# Démarrage du serveur
if __name__ == "__main__":
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Service SOAP démarré sur http://localhost:8000")
    server.serve_forever()

