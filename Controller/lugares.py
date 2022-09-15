from flask import Blueprint, jsonify, request
from Model import lugares

lugares_blueprint = Blueprint('lugares', __name__)


@lugares_blueprint.route('/adicionar_novo_lugar', methods=['GET'])
def cadastrar_lugar():
    lugar = request.json #nome_do_lugar, obs_sobre_lugar
    lugares.adicionar_novo_lugar(lugar)
    return jsonify({"mensagem": "Lugar adicionado com sucesso!"})


@lugares_blueprint.route('/editar_lugar', methods=['PATCH'])
def editar_lugar():
    lugar_editado = request.json #id_lugar, nome_do_lugar, obs_sobre_lugar
    lugares.editar_lugar(lugar_editado)
    return jsonify({"msg": "Lugar atualizado"})

@lugares_blueprint.route('/consultar_lugares', methods=['POST'])
def consultar_lugares():
    lugares_salvos = lugares.consultar_lugares_salvos()
    return jsonify(lugares_salvos)

@lugares_blueprint.route('/apagar_lugar', methods=['DELETE'])
def apagar_lugar():
    id_lugar = request.json #id_lugar
    lugares.apagar_lugar(id_lugar)
    return jsonify({"msg":"Lugar apagado com sucesso!"})