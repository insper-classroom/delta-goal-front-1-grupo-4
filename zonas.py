import json
from collections import Counter


# with open('modelo_cruzamentos.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)


# # Recalculating the zone percentages from the JSON data
# def calculate_zone_percentages(data):
#     zone_counter = Counter()

#     for team_key in data['time']:
#         rupturas = data['time'][team_key]['rupturas']
#         for ruptura in rupturas:
#             # Counting zones
#             zona = ruptura['zona']
#             zone_counter[zona] += 1

#     total_rupturas = sum(zone_counter.values())
#     zone_percentages = {zone: (count / total_rupturas) * 100 for zone, count in zone_counter.items()}

#     return zone_percentages

# zone_percentages = calculate_zone_percentages(data)

# # Formatting the result for presentation
# zone_percentages_formatted = {zone: f"{percentage:.1f}%" for zone, percentage in zone_percentages.items()}
# zone_percentages_formatted

# print(zone_percentages_formatted)

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

