import json

def parse_decks():
    parsed_data = []
    with open("api_decks.json", "r") as payload:
        data = json.load(payload)

    for deck in data:
        dc = {
            "name": deck["name"],
            "type": deck["deckType"],
            "houses": deck["housesAndCards"],
            "synergies": deck["synergyDetails"]
        }

        parsed_data.append(dc)
    
    with open("standard_decks.json", "w") as payload:
            json.dump(parsed_data, payload)
