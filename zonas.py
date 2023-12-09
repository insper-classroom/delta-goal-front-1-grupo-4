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

# def pegar_imagem(jogador):
#     lista_jogador=[{'nome': 'G. Gomez', 'imagem': 'img/gustavo_gomez_palmeiras.jpg'},
#             {'nome': 'Luan', 'imagem': 'img/luan_palmeiras.jpeg'},
#             {'nome': 'Rony', 'imagem': 'img/rony_palmeiras.jpg'},
#             {'nome': 'Fabinho', 'imagem': 'img/fabinho_palmeiras.jpg'},
#             {'nome': 'Artur', 'imagem': 'img/artur_palmeiras.jpg'},
#             {'nome': 'Sasha', 'imagem': 'img/Sasha_bragantino.png'},
#             {'nome': 'E. Santos', 'imagem': 'img/santos_bragantino.png'},
#             {'nome': 'B. Goncalves ', 'imagem': 'img/bruno_brangantino.png'},
#             {'nome': 'Natan', 'imagem': 'img/natan_bragantino.png'},
#             {'nome': 'Juninho Capixaba', 'imagem': 'img/juninho_bragantino.png'},]
    for pi in lista_jogador:
        if pi['nome']== jogador:
            return pi['imagem']

def contagem_jogadores(dados,time):
    contagem = Counter(lista_jogadores_cruzamentos(dados,time))
    lista_contagem = [{"nome": jogador, "numero": contagem[jogador]} for jogador in contagem]
    return lista_contagem

def destaque_jogadores(dados,time):
    jogadores_ordenados = sorted(contagem_jogadores(dados,time), key=lambda x: x["numero"], reverse=True)
    destaque_n_jogadores = jogadores_ordenados[:5]
    return destaque_n_jogadores


def calculate_line_break_percentages_v4(json_data, zones_of_interest):
    """
    Calculate the percentage of line breaks that occurred in each of the specified zones in the provided JSON data.
    For the second team in the JSON data, zones 'Zona 1 - A' and 'Zona 1 - B' are treated as 'Zona 3 - A' and 'Zona 3 - B' respectively.

    :param json_data: A JSON object containing the data.
    :param zones_of_interest: A list of zone names in which the line breaks are to be calculated.
    :return: A dictionary with the zone names as keys and their respective line break percentages as values.
    """
    # Initialize a dictionary to count the line breaks in each zone
    line_breaks = {zone: 0 for zone in zones_of_interest}

    # Track the team count
    team_count = 0

    # Iterate over the teams and their zones to count the line breaks
    for team_id, team_data in json_data["time"].items():
        team_count += 1
        for zone, count in team_data["zonas"].items():
            # For the first team, count normally
            if team_count == 1:
                if zone in zones_of_interest:
                    line_breaks[zone] += count
            # For the second team, adjust the zones as specified
            else:
                if zone == "Zona 1 - A":
                    line_breaks["Zona 3 - A"] += count
                elif zone == "Zona 1 - B":
                    line_breaks["Zona 3 - B"] += count
                elif zone in zones_of_interest:
                    line_breaks[zone] += count

    # Calculate the total number of line breaks
    total_line_breaks = sum(line_breaks.values())

    # Calculate the percentage of line breaks in each zone
    percentages = {zone: (count / total_line_breaks * 100) if total_line_breaks > 0 else 0 for zone, count in line_breaks.items()}

    return percentages

# Example usage of the revised function
zones_of_interest_v4 = ["Zona 1 - A", "Zona 1 - B", "Zona 2", "Zona 3 - A", "Zona 3 - B"]
with open('dados/modelo_quebra_linha.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def aaaa(data):
    pal= data['time']['1']["desfechos"]
    rdd= data['time']['5']["desfechos"]
    dic_g={}
    dic={}
    dic['pal']=pal
    dic['red']=rdd
    dic_g['desfechos']= dic
    dic_g['ok']= True
    return dic_g
print(aaaa(data))
