import sqlite3

def formatar_historico_para_json(historico):
    historico_json = {}
    for item in historico:
        historico_json[f"{item[0]}"] = {"distancia":item[1],"espessura_tabela":item[2],"atividade_fonte":item[3],"data_do_calculo":item[4],"fk_lugar":item[5]}
    return historico_json


def adicionar_calculo_historico(valores):
    conexao = sqlite3.connect('.\Model\calculos_historico.db')
    cursor = conexao.cursor()
    distancia = valores["distancia"]
    espessura_tab = valores["espessura_tabela"]
    atividade_fonte = valores["atividade_fonte"]
    classe_filme = valores["classe_filme"]
    fk_lugar = valores["fk_lugar"]
    comando =   f"""INSERT INTO tbl_calculos_historico(distancia, espessura_tabela, atividade_fonte, classe_filme, fk_lugar, data_do_calculo)
                        VALUES (
                            {distancia},
                            {espessura_tab},
                            {atividade_fonte},
                            {classe_filme},
                            {fk_lugar},
                            datetime('now')
                        )"""
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_calculo():
    conexao = sqlite3.connect('.\Model\calculos_historico.db')
    cursor = conexao.cursor()
    comando = f""" SELECT * FROM tbl_calculos_historico """
    cursor.execute(comando)
    historico = cursor.fetchall()
    historico_json = formatar_historico_para_json(historico)
    cursor.close()
    conexao.close()
    return historico_json

def apagar_calculo(id):
    conexao = sqlite3.connect('.\Model\calculos_historico.db')
    cursor = conexao.cursor()
    comando = f""" DELETE FROM tbl_calculos_historico WHERE id_calculo = {id['id_calculo']}"""
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
