import json

def aerc_count(decks: list):
    data = []
    i = 1
    for deck in decks:
        print("{} --> {}".format(i, deck["name"]))
        i += 1

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
        # print(ctrl)
    delta_sasb_arcb = 0
    delta_sasb_arcc = 0
    delta_sasc_arcb = 0
    delta_sasc_arcc = 0

    for item in data:
            delta_sasb_arcb += abs(item["sasb_aercb"] - item["sas"])
            delta_sasb_arcc += abs(item["sasb_aercc"] - item["sas"])
            delta_sasc_arcb += abs(item["sasc_aercb"] - item["sas"])
            delta_sasc_arcc += abs(item["sasc_aercc"] - item["sas"])
    data.append({
            "delta_sasb_aercb": delta_sasb_arcb,
            "delta_sasb_aercc": delta_sasb_arcc,
            "delta_sasc_aercb": delta_sasc_arcb,
            "delta_sasc_aercc": delta_sasc_arcc,
    })

    with open("sas_log.json", "w") as payload:
            json.dump(data, payload)
