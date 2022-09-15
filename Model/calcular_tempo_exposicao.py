def calcular_tempo_exposicao(valores):
    d = float(valores["distancia"])
    tab = float(valores["espessura_tabela"])
    a = float(valores["atividade_fonte"])
    cf = float(valores["classe_filme"])
    tempo_exposicao = {'tempo_exposicao': d**2*tab/a/cf}
    return tempo_exposicao