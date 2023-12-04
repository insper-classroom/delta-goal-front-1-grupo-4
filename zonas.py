import json
from collections import Counter

def contar_zonas_repetidas(dados,time):
    palmeiras_rupturas = dados["time"][time]["rupturas"]
    zonas_repetidas = {}

    for ruptura in palmeiras_rupturas:
        zona = ruptura["zona"]

        if zona in zonas_repetidas:
            zonas_repetidas[zona] += 1
        else:
            zonas_repetidas[zona] = 1

    return zonas_repetidas

def calculate_zone_percentages(dados,time):
    dicionario=contar_zonas_repetidas(dados,time)
    total=0
    for quantidade in dicionario.values():
        total+=quantidade
    for zona, cru in dicionario.items():
        dicionario[zona]=f"{(cru/total)*100:.1f}%"
    return dicionario


def lista_jogadores_cruzamentos(dados, time):
    jogadores = []

    if time in dados["time"]:
        rupturas_time = dados["time"][time]["rupturas"]

        for ruptura in rupturas_time:
            jogadores_cruzando = ruptura["nome_jogadores_time_cruzando"]
            nomes = jogadores_cruzando.split(", ")
            jogadores.extend(nomes)

    return jogadores

def pegar_imagem(jogador):
    lista_jogador=[{'nome': 'G Gomez', 'imagem': 'img/gustavo_gomez_palmeiras.jpg'},
            {'nome': 'Luan', 'imagem': 'img/luan_palmeiras.jpeg'},
            {'nome': 'Rony ', 'imagem': 'img/rony_palmeiras.jpg'},
            {'nome': 'Fabinho', 'imagem': 'img/fabinho_palmeiras.jpg'},
            {'nome': 'Artur', 'imagem': 'img/artur_palmeiras.jpg'},
            {'nome': 'Sasha', 'imagem': 'img/Sasha_bragantino.png'},
            {'nome': 'E. Santos ', 'imagem': 'img/santos_bragantino.png'},
            {'nome': 'B. Goncalves	', 'imagem': 'img/bruno_brangantino.png'},
            {'nome': 'Natan', 'imagem': 'img/natan_bragantino.png'},
            {'nome': 'Juninho Capixaba	', 'imagem': 'img/juninho_bragantino.png'},]
    for pi in lista_jogador:
        if pi['nome']== jogador:
            return pi['imagem']

def contagem_jogadores(dados,time):
    contagem = Counter(lista_jogadores_cruzamentos(dados,time))
    lista_contagem = [{"nome": jogador, "numero": contagem[jogador], 'imagem':pegar_imagem[jogador]} for jogador in contagem]
    return lista_contagem

def destaque_jogadores(dados,time):
    jogadores_ordenados = sorted(contagem_jogadores(dados,time), key=lambda x: x["numero"], reverse=True)
    destaque_n_jogadores = jogadores_ordenados[:5]
    return destaque_n_jogadores


with open('modelo_cruzamentos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

p=pegar_imagem('G Gomez')
print(p)