import json

from numpy import argsort, array

from utils.get_atr import get_atr
from utils.min_max import normalize_by_min_max


class GeneticAlgorithm:
    decks_atr = {}
    norm_decks_atr = {}
    weight = {"ac": 2.12, "cc": 1.76, "cp": 13.3, "ep": 0.2612, "ea": 3.0, "dr": 1.5}
    values = []

    def __init__(self, weight: dict = None):
        """
        "weight" param must contain: {ac, cc, cp, ep, ea, dr} as keys.\n
        """

        if weight:
            self.weight = weight

    def create_deck_atr(self, file: str = "standard_decks.json"):
        with open(file, "r") as load:
            data = json.load(load)

        for deck in data:
            self.decks_atr[deck["name"]] = get_atr(deck)

    def atr_normalization(self):
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
