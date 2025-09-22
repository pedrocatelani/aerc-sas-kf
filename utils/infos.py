import os
import json


def get_infos(deck: int, file: dict) -> tuple:
    d = file[deck]
    infos = []
    houses = []

    for house in d["houses"]:
        name = house["name"]
        houses.append(name)
        inf = {
            "name": name,
            "expectedAmber": 0.0,
            "amberControl": 0.0,
            "creatureControl": 0.0,
            "effectivePower": 0.0,
            "creatureProtection": 0.0,
            "disruption": 0.0,
        }
        for syn in d["synergies"]:
            if syn["house"] == name:
                inf["expectedAmber"] += syn["expectedAmber"]
                inf["amberControl"] += syn["amberControl"]
                inf["creatureControl"] += syn["creatureControl"]
                inf["effectivePower"] += syn["effectivePower"]
                inf["creatureProtection"] += syn["creatureProtection"]
                inf["disruption"] += syn["disruption"]

        infos.append(inf)

    return (d["name"], houses, infos)


os.system("cls")
choice = input("> Select your desired file!\n[1]-Standard\n[2]-Aliance\n\n-->")
file = "standard_decks.json" if choice == "1" else "aliance_decks.json"

os.system("cls")
with open(file, "r") as decks_file:
    decks = json.load(decks_file)

    while True:
        count = 0
        for d in decks:
            print(f"{count} - {d["name"]}")
            count += 1

        get = int(input("\n>Deck to see:   "))

        name, houses, infos = get_infos(get, decks)

        while True:
            os.system("cls")
            print("-" * 30)
            print("{}".format(name))
            print("-" * 30)
            count = 0
            for house in houses:
                print("[{}] - {}".format(count, house))
                count += 1
            print("[3] - All")
            print("[4] - Every")
            print("[5] - Break")

            choice = int(input("\n> Selecione:  "))

            os.system("cls")
            print("-" * 30)
            print("{}".format(name))
            print("-" * 30)

            if choice < 3:
                get = infos[choice]
                print(get["name"])
                print("expectedAmber", get["expectedAmber"])
                print("amberControl", get["amberControl"])
                print("effectivePower", get["effectivePower"])
                print("creatureProtection", get["creatureProtection"])
                print("creatureControl", get["creatureControl"])
                print("disruption", get["disruption"])
            elif choice == 3:
                for d in infos:
                    print("-" * 30)
                    print(d["name"])
                    print("expectedAmber", d["expectedAmber"])
                    print("amberControl", d["amberControl"])
                    print("effectivePower", d["effectivePower"])
                    print("creatureProtection", d["creatureProtection"])
                    print("creatureControl", d["creatureControl"])
                    print("disruption", d["disruption"])
            elif choice == 4:
                inf = {
                    "name": "WholeDeck//EveryHouse",
                    "expectedAmber": 0.0,
                    "amberControl": 0.0,
                    "creatureControl": 0.0,
                    "effectivePower": 0.0,
                    "creatureProtection": 0.0,
                    "disruption": 0.0,
                }
                for d in infos:
                    inf["expectedAmber"] += d["expectedAmber"]
                    inf["amberControl"] += d["amberControl"]
                    inf["creatureControl"] += d["creatureControl"]
                    inf["effectivePower"] += d["effectivePower"]
                    inf["creatureProtection"] += d["creatureProtection"]
                    inf["disruption"] += d["disruption"]

                print(inf["name"])
                print("expectedAmber", inf["expectedAmber"])
                print("amberControl", inf["amberControl"])
                print("effectivePower", inf["effectivePower"])
                print("creatureProtection", inf["creatureProtection"])
                print("creatureControl", inf["creatureControl"])
                print("disruption", inf["disruption"])
            else:
                os.system("cls")
                break

            input()
