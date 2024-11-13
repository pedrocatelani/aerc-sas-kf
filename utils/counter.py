import json

def aerc_count(decks: list):
    data = []
    for deck in decks:
        print(deck["name"])

        aerc_raw = 0
        aerc_complete = 0
        sas_raw = 0
        sas_complete = 0
        ctrl = 0

        for card in deck["synergyDetails"]:
            ctrl += 1
            aerc_raw += card["aercScore"]
            sas_raw += card["netSynergy"]
            aerc_complete += card["aercScore"] * card["copies"]
            sas_complete += card["netSynergy"] * card["copies"]

        data.append(
            {
                "name": deck["name"],
                "sas": deck["sasRating"],
                "aerc_base": aerc_raw,
                "aerc_comp": aerc_complete,
                "sas_base": sas_raw,
                "sas_comp": sas_complete,
                "sasb_aercb": sas_raw + aerc_raw,
                "sasb_aercc": sas_raw + aerc_complete,
                "sasc_aercb": sas_complete + aerc_raw,
                "sasc_aercc": sas_complete + aerc_complete,
            }
        )
        print(ctrl)

    with open("results.json", "w") as payload:
            json.dump(data, payload)