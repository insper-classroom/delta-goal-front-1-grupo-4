import json
from collections import Counter



with open('modelo_cruzamentos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def extrair_areas(data):
    areas = set()

    for team_key in data['time']:
        rupturas = data['time'][team_key]['rupturas']
        for ruptura in rupturas:
            # Adiciona a área da ruptura ao conjunto
            areas.add(ruptura['zona'])

    return areas

# Chamada da função para extrair as áreas
areas = extrair_areas(data)
print(areas)

def detalhar_cruzamentos(dados):
    cruzamentos = []

    for team_data in dados.values():
        for ruptura in team_data['rupturas']:
            cruzamento_info = {
                "instante_cruzamento": ruptura['instante_cruzamento'],
                "jogadores_atacando": ruptura['nome_jogadores_time_cruzando'],
                "jogadores_defendendo": ruptura['nome_jogadores_time_defendendo'],
                "desfecho": ruptura['desfecho'],
                "zona": ruptura['zona']
            }
            cruzamentos.append(cruzamento_info)
    return cruzamentos


def analisar_destaques(dados):
    jogadores_ataque = []
    jogadores_defesa = []
    zonas = []
    desfechos = []

    for team_data in dados.values():
        for ruptura in team_data['rupturas']:
            jogadores_ataque.extend(ruptura['nome_jogadores_time_cruzando'].split(', '))
            jogadores_defesa.extend(ruptura['nome_jogadores_time_defendendo'].split(', '))
            zonas.append(ruptura['zona'])
            desfechos.append(ruptura['desfecho'])

    destaques = {
        'jogadores_ataque': Counter(jogadores_ataque).most_common(7),
        'jogadores_defesa': Counter(jogadores_defesa).most_common(7),
        'zonas': Counter(zonas).most_common(20),
        'desfechos': Counter(desfechos).most_common()
    }
    return destaques




# Primeiro, você chama as funções com os dados carregados
destaques = analisar_destaques(data['time'])
cruzamentos = detalhar_cruzamentos(data['time'])

# Para imprimir os destaques
print("Destaques dos Cruzamentos:")
print("Jogadores Mais Frequentes no Ataque:", destaques['jogadores_ataque'])
print("Jogadores Mais Frequentes na Defesa:", destaques['jogadores_defesa'])
print("Zonas Mais Comuns de Cruzamento:", destaques['zonas'])
print("Desfechos dos Cruzamentos:", destaques['desfechos'])

# Para imprimir os detalhes de cada cruzamento
print("\nDetalhes dos Cruzamentos:")
for cruzamento in cruzamentos:
    print(f"Cruzamento às {cruzamento['instante_cruzamento']}:")
    print("  Jogadores Atacando:", cruzamento['jogadores_atacando'])
    print("  Jogadores Defendendo:", cruzamento['jogadores_defendendo'])
    print("  Desfecho:", cruzamento['desfecho'])
    print("  Zona:", cruzamento['zona'])
    print()

from collections import Counter

# Function to process the data and extract the required information
def process_data(data):
    zone_counter = Counter()
    player_counter = Counter()

    for team_key in data['time']:
        rupturas = data['time'][team_key]['rupturas']
        for ruptura in rupturas:
            # Counting zones
            zona = ruptura['zona']
            zone_counter[zona] += 1

            # Counting players in successful ruptures
            if ruptura['desfecho'] == 'Bem-Sucedido':
                players = ruptura['nome_jogadores_time_cruzando'].split(',')
                for player in players:
                    player_counter[player.strip()] += 1

    total_rupturas = sum(zone_counter.values())
    zone_percentages = {zone: (count / total_rupturas) * 100 for zone, count in zone_counter.items()}

    return zone_counter, zone_percentages, player_counter

zone_counter, zone_percentages, player_counter = process_data(data)

zone_counter, zone_percentages, player_counter.most_common(20)  # Displaying top 5 players for highlight

print("Zonas Mais Comuns de Cruzamento:", zone_counter)
print("Zonas Mais Comuns de Cruzamento:", zone_percentages)
print("Jogadores Mais Frequentes no Ataque:", player_counter.most_common(5))
