import json
from collections import Counter



with open('modelo_cruzamentos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def extrair_informacoes_palmeiras(data, nome_time='Palmeiras'):
    info_jogo_palmeiras = []

    for team_key, team_data in data['time'].items():
        if team_data['nome'] == nome_time:
            for ruptura in team_data['rupturas']:
                info_ruptura = {
                    'instante_inicial': ruptura['instante_cruzamento'],
                    'jogadores_envolvidos': ruptura['nome_jogadores_time_cruzando'],
                    "jogadores_defendendo": ruptura['nome_jogadores_time_defendendo'],
                    'desfecho': ruptura['desfecho'],
                    'zona': ruptura['zona']
                }
                info_jogo_palmeiras.append(info_ruptura)
            break

    return info_jogo_palmeiras

# Supondo que 'data' é o seu JSON carregado
informacoes_palmeiras = extrair_informacoes_palmeiras(data)
print(informacoes_palmeiras)