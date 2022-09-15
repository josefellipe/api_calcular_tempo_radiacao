from flask import Blueprint, jsonify, request
from Model import calcular_tempo_exposicao, calculos


calculos_blueprint = Blueprint('calculos', __name__)

@calculos_blueprint.route('/novo_calculo', methods=['GET'])
def calcular_tempo():
    medidas = request.json #distancia, espessura_tabela, atividade_fonte, classe_filme, "id_lugar"
    tempo = calcular_tempo_exposicao.calcular_tempo_exposicao(medidas)
    calculos.adicionar_calculo_historico(medidas)
    return jsonify(tempo)

@calculos_blueprint.route('/consultar_historico', methods=['POST'])
def consultar_historico_calculos():
    consulta = calculos.consultar_calculo()
    return jsonify(consulta)

@calculos_blueprint.route('/deletar_calculo', methods=['DELETE'])
def deletar_historico_calculo():
    id_para_deletar = request.json
    calculos.apagar_calculo(id_para_deletar)
    return jsonify({"msg": "Calculo removido do histótico" })