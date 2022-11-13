from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)


from controladores.controlador_partidosPoliticos import controlador_partidosPoliticos
micontroladorPartidosPoliticos = controlador_partidosPoliticos()

#Microservicio de Creacion
@app.route("/partidospoliticos",methods=['POST'])
def crearPartidoPolitico():
    datos = request.get_json()
    json = micontroladorPartidosPoliticos.create(datos)
    return jsonify(json)

#Microservicio de listado
@app.route("/partidospoliticos",methods=['GET'])
def listarPartidoPolitico():
    json = micontroladorPartidosPoliticos.index()
    return jsonify(json)

#Microservicio de Borrado
@app.route("/partidospoliticos/<string:id>",methods=['DELETE'])
def borrarPartidoPolitico(id):
    json = micontroladorPartidosPoliticos.delete(id)
    return jsonify(json)

#Microservicio de Actualizacion
@app.route("/partidopolitico/<string:id>",methods = ['PUT'])
def actualizarPartidoPolitico(id):
    data = request.get_json()
    json = micontroladorPartidosPoliticos.update(id,data)
    return jsonify(json)

#Microservicio de Consulta
@app.route("/partidopolitico/<string:id>",methods = ['GET'])
def consultarPartidoPolitico(id):
    json = micontroladorPartidosPoliticos.show(id)
    return jsonify(json)








"""@app.route("/",methods=['GET'])
def msPrueba():
    json = {}
    json["message"] = "Mi primer microservicio con Flask"
    return jsonify(json)"""

def cargueConfigFile():
    with open('config.json') as file:
        datos = json.load(file)
    return datos

def print_hi(name):
    print(f'Hi, {name}')

if __name__=='__main__':
    print_hi('Grupo 32')
    configData = cargueConfigFile()
    print("Servidor Ejecutandose en: "+"http://"+configData["url-backend"]+":" + str(configData["port"]))
    serve(app,host=configData["url-backend"],port=configData["port"])

