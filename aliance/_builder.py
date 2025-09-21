import random as rd
import json


def build(self):
    data = {}
    for deck in self.standard_decks:
        data[deck["name"]] = [
            deck["houses"][0]["name"],
            deck["houses"][1]["name"],
            deck["houses"][2]["name"],
        ]

    self.available_decks = data
    self.aliance_decks = (
        self.build_sequential() if self.mode == "SEQUENTIAL" else self.build_random()
    )


def create(self):
    x = 1
    parsed_data = []
    for deck in self.selected_decks:

        entry = {
            "name": "Aliance{0}".format(x),
            "type": "ALIANCE",
            "houses": [],
            "synergies": [],
        }

        for house in deck:

            for std_deck in self.standard_decks:

                if std_deck["name"] == house[0]:
                    for h in std_deck["houses"]:

                        if h["name"] == house[1]:
                            entry["houses"].append(
                                {
                                    "name": h["name"],
                                    "parent": std_deck["name"],
                                    "cards": h["cards"],
                                }
                            )
                    for s in std_deck["synergies"]:

                        if s["house"] == house[1]:
                            entry["synergies"].append(
                                {
                                    "house": s["house"],
                                    "cardName": s["cardName"],
                                    "synergies": s["synergies"],
                                    "netSynergy": s["netSynergy"],
                                    "aercScore": s["aercScore"],
                                    "expectedAmber": s["expectedAmber"],
                                    "amberControl": s["amberControl"],
                                    "creatureControl": s["creatureControl"],
                                    "artifactControl": s["artifactControl"],
                                    "efficiency": s["efficiency"],
                                    "recursion": s["recursion"],
                                    "effectivePower": s["effectivePower"],
                                    "creatureProtection": s["creatureProtection"],
                                    "disruption": s["disruption"],
                                    "other": s["other"],
                                    "copies": s["copies"],
                                    "notCard": s["notCard"],
                                    "synStart": s["synStart"],
                                }
                            )
        parsed_data.append(entry)
        x += 1

    print(f"-- Builded {x} decks!")
    with open("aliance_decks.json", "w") as payload:
        json.dump(parsed_data, payload)


def build_sequential(self):
    count = 1
    for deck1 in self.available_decks:
        house1 = self.available_decks[deck1][0]

        for deck2 in self.available_decks:
            house2 = self.available_decks[deck2][1]

            if house2 != house1:
                for deck3 in self.available_decks:
                    house3 = self.available_decks[deck3][2]

                    if house3 != house1 and house3 != house2:
                        if self.create_name(
                            deck1, deck2, deck3, house1, house2, house3
                        ):
                            count += 1
    self.create()


def build_random(self):
    count = 0
    while count <= len(self.available_decks.keys()) * 1.375:
        deck1 = rd.choice(list(self.available_decks.keys()))
        house1 = self.available_decks[deck1][rd.randint(0, 2)]
        deck2 = rd.choice(list(self.available_decks.keys()))
        house2 = self.available_decks[deck2][rd.randint(0, 2)]
        deck3 = rd.choice(list(self.available_decks.keys()))
        house3 = self.available_decks[deck3][rd.randint(0, 2)]

        if house1 == house2 or house2 == house3 or house1 == house3:
            pass
        else:
            if self.create_name(deck1, deck2, deck3, house1, house2, house3):
                count += 1
    self.create()


def create_name(self, deck1, deck2, deck3, house1, house2, house3) -> bool:
    names = [f"{deck1}-{house1} ", f"{deck2}-{house2} ", f"{deck3}-{house3} "]
    names.sort()
    name = ""
    for n in names:
        name += n
    if name not in self.selected_decks_keys:
        self.selected_decks_keys.append(name)

        self.selected_decks.append(
            [
                [deck1, house1],
                [deck2, house2],
                [deck3, house3],
            ]
        )
        return True
    return False
