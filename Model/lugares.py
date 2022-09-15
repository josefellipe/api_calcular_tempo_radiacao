import sqlite3
from flask import jsonify

def transformar_em_json(historico):
    historico_json = {}
    for item in historico:
        historico_json[f"'{item[0]}'"] = {"nome_do_lugar":item[1], "obs_sobre_lugar": item[2]}
    return historico_json



def adicionar_novo_lugar(lugar):
    conexao = sqlite3.connect('.\Model\calculos_historico.db')
    cursor = conexao.cursor()
    nome_lugar = lugar["nome_do_lugar"]
    obs_lugar = lugar["obs_sobre_lugar"]
    comando = f"""INSERT INTO tbl_lugares(nome_do_lugar, obs_sobre_lugar)
                    VALUES (
                        '{nome_lugar}',
                        '{obs_lugar}'
                            )"""
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()


def consultar_lugares_salvos():
    conexao = sqlite3.connect('.\Model\calculos_historico.db')
    cursor = conexao.cursor()
    comando = f"""SELECT * FROM tbl_lugares"""
    cursor.execute(comando)
    historico = cursor.fetchall()
    historico_json = transformar_em_json(historico)
    return historico_json


def editar_lugar(lugar):
    conexao = sqlite3.connect('.\Model\calculos_historico.db')
    cursor = conexao.cursor()
    id_lugar = lugar["id_lugar"]
    novo_nome = lugar["nome_do_lugar"]
    nova_obs = lugar["obs_sobre_lugar"]
    comando = f"""UPDATE tbl_lugares SET nome_do_lugar = '{novo_nome}', obs_sobre_lugar = '{nova_obs}' WHERE id_lugar = {id_lugar}"""
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def apagar_lugar(id):
    conexao = sqlite3.connect('.\Model\calculos_historico.db')
    cursor = conexao.cursor()
    comando = f"""DELETE FROM tbl_lugares WHERE id_lugar = {id["id_lugar"]}"""
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()