import json
import random


class BattleSim:
    deck_1 = None
    deck_2 = None
    player_1_hand = None
    player_2_hand = None
    first_player = None
    deck_list = None
    battle_round = 1

    def __init__(self, mode: str = "STANDARD"):
        if mode == "STANDARD":
            deck_file = "standard_decks.json"

        with open(deck_file, "r") as payload:
            self.deck_list = json.load(payload)
        
        self.deck_1 = self.deck_list[0]
        self.deck_2 = self.deck_list[1]

        self.first_player = f"deck_{random.randint(1,2)}"
