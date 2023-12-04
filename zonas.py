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


# Exemplo de uso
with open('modelo_cruzamentos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

#percentual do palmeiras
# Formatting the result for presentation
zone_percentages_formatted = calculate_zone_percentages(data,'1')
zone_percentages_formatted

#percentual do bragantino 
zone_percentages_bragantino = calculate_zone_percentages(data,'5')
print(zone_percentages_bragantino)

