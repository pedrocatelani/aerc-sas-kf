import json

def parse_decks():
    print("\n\n>> Iniciando tratativa de informações...\n")
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
    
    print(">> Processo finalizado!\n\n")
    print(">> Teste outras funções da main!!!\n")
    print(">> python main.py --GA  <Genetic Algorithm>")
    print(">> python main.py --BL  <Battle Loop>")
    with open("standard_decks.json", "w") as payload:
            json.dump(parsed_data, payload)

