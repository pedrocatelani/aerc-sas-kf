import json


def attr_average():
    ctrl = 0
    expected_amber = 0
    amber_control = 0
    creature_control = 0
    creature_protection = 0
    effective_power = 0
    disruption = 0

    with open("aliance_decks.json", "r") as load:
        data = json.load(load)

        for deck in data:
            ctrl += 1

            for attr in deck["synergies"]:
                expected_amber += attr["expectedAmber"]
                amber_control += attr["amberControl"]
                creature_control += attr["creatureControl"]
                creature_protection += attr["creatureProtection"]
                effective_power += attr["effectivePower"]
                disruption += attr["disruption"]

        print(
            f"AE: {expected_amber/ctrl}\nCA: {amber_control/ctrl}\nCC: {creature_control/ctrl}\nCP: {creature_protection/ctrl}\nEF: {effective_power/ctrl}\nDR: {disruption/ctrl}"
        )
