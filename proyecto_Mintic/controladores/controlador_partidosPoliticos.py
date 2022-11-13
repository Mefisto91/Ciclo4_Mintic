import self as self

from modelos.partidospoliticos import partidospoliticos

class controlador_partidosPoliticos():
    def __init__(self):
        print("creando controlador de partidos politicos")

    def index(self):
        print("listado de todos los partidos politicos")
        unpartidoPolitico = {
            "_idpartido": "abc123",
            "codigo": "123",
            "nombre": "Pacto Historico",
            "lema": "Lucha por la vida"
        }
        return[unpartidoPolitico]

    def create(self, elpartidosPoliticos):
        print("crea un partido politico")
        partido_politico = partidospoliticos(elpartidosPoliticos)
        return partido_politico.__dict__


    def show(self, id):
        print("mostrando un partido politico con id ",id)
        elpartidoPolitico ={
            "id": id,
            "codigo": "123",
            "nombre": "Pacto Historico",
            "lema": "Lucha por la vida"
        }
        return elpartidoPolitico

    def update(self, id, elpartidosPoliticos):
        print("Actualizando partidos politicos con id ",id)
        elpartidoPolitico = partidospoliticos(elpartidosPoliticos)
        return elpartidoPolitico.__dict__

    def delete(self, id):
        print("Eliminando partidos politicos con id ", id)
        return {"partido politico borrado:": id}

