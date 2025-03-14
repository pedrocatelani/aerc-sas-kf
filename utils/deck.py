import json

def parse_decks():
    parsed_data = []
    with open("api_decks.json", "r") as payload:
        data = json.load(payload)

    for deck in data:
        houses = []
        for house in deck["housesAndCards"]:
            house_dict = {
                "name": house["house"],
                "cards": []
            }
            for card in house["cards"]:
                 house_dict["cards"].append([house["house"],card["cardTitle"]])
            
            houses.append(house_dict)

        dc = {
            "name": deck["name"],
            "type": deck["deckType"],
            "houses": houses,
            "synergies": deck["synergyDetails"]
        }

        parsed_data.append(dc)
    
    with open("standard_decks.json", "w") as payload:
            json.dump(parsed_data, payload)
