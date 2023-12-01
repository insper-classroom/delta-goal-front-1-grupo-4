import json
from collections import Counter


with open('modelo_cruzamentos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# Recalculating the zone percentages from the JSON data
def calculate_zone_percentages(data):
    zone_counter = Counter()

    for team_key in data['time']:
        rupturas = data['time'][team_key]['rupturas']
        for ruptura in rupturas:
            # Counting zones
            zona = ruptura['zona']
            zone_counter[zona] += 1

    total_rupturas = sum(zone_counter.values())
    zone_percentages = {zone: (count / total_rupturas) * 100 for zone, count in zone_counter.items()}

    return zone_percentages

zone_percentages = calculate_zone_percentages(data)

# Formatting the result for presentation
zone_percentages_formatted = {zone: f"{percentage:.1f}%" for zone, percentage in zone_percentages.items()}
zone_percentages_formatted

print(zone_percentages_formatted)
