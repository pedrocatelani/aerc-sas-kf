import json

import random as rd
from numpy import argsort, array

from utils.get_atr import get_atr
from utils.min_max import normalize_by_min_max


class GeneticAlgorithm:
    decks_atr = {}
    norm_decks_atr = {}
    file = ""
    weight = {"ac": 2.12, "cc": 1.76, "cp": 13.3, "ep": 0.2612, "ea": 3.0, "dr": 1.5}
    values = []

    def __init__(self, weight: dict = None, file: str = "standard_decks.json"):
        """
        "weight" param must contain: {ac, cc, cp, ep, ea, dr} as keys.\n
        "file" is a string path to the decks json. \n
        """

        if weight:
            self.weight = weight
        if file:
            self.file = file

    def create_deck_atr(self, file: bool = None):
        file_string = file if file else self.file
        self.decks_atr = {}
        with open(file_string, "r") as load:
            data = json.load(load)

        for deck in data:
            self.decks_atr[deck["name"]] = get_atr(deck)

    def atr_normalization(self):
        self.norm_decks_atr = {}
        max_ea = max(self.decks_atr.values(), key=lambda x: x["expectedAmber"])[
            "expectedAmber"
        ]
        max_ac = max(self.decks_atr.values(), key=lambda x: x["amberControl"])[
            "amberControl"
        ]
        max_cc = max(self.decks_atr.values(), key=lambda x: x["creatureControl"])[
            "creatureControl"
        ]
        max_cp = max(self.decks_atr.values(), key=lambda x: x["creatureProtection"])[
            "creatureProtection"
        ]
        max_ep = max(self.decks_atr.values(), key=lambda x: x["effectivePower"])[
            "effectivePower"
        ]
        max_dr = max(self.decks_atr.values(), key=lambda x: x["disruption"])[
            "disruption"
        ]

        min_ea = min(self.decks_atr.values(), key=lambda x: x["expectedAmber"])[
            "expectedAmber"
        ]
        min_ac = min(self.decks_atr.values(), key=lambda x: x["amberControl"])[
            "amberControl"
        ]
        min_cc = min(self.decks_atr.values(), key=lambda x: x["creatureControl"])[
            "creatureControl"
        ]
        min_cp = min(self.decks_atr.values(), key=lambda x: x["creatureProtection"])[
            "creatureProtection"
        ]
        min_ep = min(self.decks_atr.values(), key=lambda x: x["effectivePower"])[
            "effectivePower"
        ]
        min_dr = min(self.decks_atr.values(), key=lambda x: x["disruption"])[
            "disruption"
        ]

        for key, values in self.decks_atr.items():
            self.norm_decks_atr[key] = {
                "expectedAmber": normalize_by_min_max(
                    values["expectedAmber"], min_ea, max_ea
                ),
                "amberControl": normalize_by_min_max(
                    values["amberControl"], min_ac, max_ac
                ),
                "creatureControl": normalize_by_min_max(
                    values["creatureControl"], min_cc, max_cc
                ),
                "creatureProtection": normalize_by_min_max(
                    values["creatureProtection"], min_cp, max_cp
                ),
                "effectivePower": normalize_by_min_max(
                    values["effectivePower"], min_ep, max_ep
                ),
                "disruption": normalize_by_min_max(
                    values["disruption"], min_dr, max_dr
                ),
            }

    def objective_function(self, atr: dict, weight: dict) -> float:
        value = (
            (atr["expectedAmber"] ** weight["ea"])
            * (atr["amberControl"] ** weight["ac"])
            * (atr["creatureControl"] ** weight["cc"])
            * (atr["creatureProtection"] ** weight["cp"])
            * (atr["effectivePower"] ** weight["ep"])
            * (atr["disruption"] ** weight["dr"])
        ) ** (
            1
            / (
                weight["ea"]
                + weight["ac"]
                + weight["cc"]
                + weight["cp"]
                + weight["ep"]
                + weight["dr"]
            )
        )

        return value * 10

    def evaluate(self) -> array:
        self.values = []
        original_decks = list(self.norm_decks_atr.values())
        v = []

        for k, d in self.norm_decks_atr.items():
            deck_value = self.objective_function(d, self.weight)

            self.values.append({"value": deck_value, "deck": k})
            v.append(deck_value)

        indexes = argsort(v)
        self.ordered_population = [original_decks[i] for i in indexes]
        self.values = [self.values[i] for i in indexes]
        v = [v[i] for i in indexes]

        return array(v)

    def cross_shuffle(self, prog_1: str, prog_2: str, file: str = None) -> tuple:
        first_progenitor = {}
        second_progenitor = {}
        first_houses = []
        second_houses = []

        file_string = file if file else self.file

        with open(file_string, "r") as load:
            data = json.load(load)

            for d in data:
                if d["name"] == prog_1:
                    first_progenitor = d.copy()
                if d["name"] == prog_2:
                    second_progenitor = d.copy()

            load.close()

        first_houses = [h["name"] for h in first_progenitor["houses"]]
        second_houses = [h["name"] for h in second_progenitor["houses"]]
        if prog_1 == prog_2:
            return (
                {prog_1: first_houses},
                {prog_1: first_houses},
            )

        all_houses = len(set(first_houses + second_houses))

        if all_houses == 6:
            rd.shuffle(first_houses)
            rd.shuffle(second_houses)

            first_descendant = {
                first_progenitor["name"]: list(first_houses[0:2]),
                second_progenitor["name"]: [second_houses[2]],
            }

            second_descendant = {
                first_progenitor["name"]: [first_houses[2]],
                second_progenitor["name"]: list(second_houses[0:2]),
            }
        elif all_houses == 3:
            first_houses.sort()
            second_houses.sort()

            first_descendant = {
                first_progenitor["name"]: [first_houses[0]],
                second_progenitor["name"]: second_houses[1:3],
            }

            second_descendant = {
                first_progenitor["name"]: first_houses[1:3],
                second_progenitor["name"]: [second_houses[0]],
            }
        else:
            commom_houses = list(set(first_houses) & set(second_houses))

            first_descendant = {
                first_progenitor["name"]: commom_houses,
                second_progenitor["name"]: list(
                    set(second_houses) - set(commom_houses)
                ),
            }

            second_descendant = {
                first_progenitor["name"]: list(set(first_houses) - set(commom_houses)),
                second_progenitor["name"]: commom_houses,
            }

        return (first_descendant, second_descendant)

    def build_descendants(
        self, build_guide: list, gen: int, file: str = None, first: bool = False
    ) -> None:
        # [{nome: [casas]}, {nome: [casas]}] --fomato esperado
        file_string = file if file else self.file
        deck_number = 1
        original_decks = {}
        descendants = []

        with open(file_string, "r") as load:
            data = json.load(load)
            for d in data:
                original_decks[d["name"]] = d

            for deck in build_guide:
                print(deck)
                new_deck = {
                    "name": "GEN{} - {}".format(gen, deck_number),
                    "type": "GA ALLIANCE",
                    "houses": [],
                    "synergies": [],
                }
                deck_number += 1

                aux_houses = {}
                for k, v in deck.items():
                    for h in original_decks[k]["houses"]:
                        aux_houses[h["name"]] = h["cards"]

                    for house in v:
                        if first:
                            new_deck["houses"].append(
                                {
                                    "name": house,
                                    "progenitor": k,
                                    "cards": [{"father": k}, *aux_houses[house]],
                                }
                            )
                        else:
                            new_deck["houses"].append(
                                {
                                    "name": house,
                                    "progenitor": k,
                                    "cards": aux_houses[house],
                                }
                            )

                        for syn in original_decks[k]["synergies"]:
                            if syn["house"] == house:
                                new_deck["synergies"].append(syn)

                descendants.append(new_deck)
                # print(new_deck)
            load.close()

            with open("ga_currentgen_decks.json", "w") as payload:
                json.dump(descendants, payload)
