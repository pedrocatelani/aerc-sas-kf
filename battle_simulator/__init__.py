import json
import random


class BattleSim:
    deck_1 = None
    deck_2 = None

    deck_1_values = None
    deck_2_values = None

    deck_1_pool = None
    deck_2_pool = None

    deck_1_pool_game = None
    deck_2_pool_game = None

    player_1_hand = []
    player_2_hand = []

    first_player = None
    deck_list = None
    battle_round = 1

    from ._turn import create_deck_pool, draw, create_card_values
    from ._battle import battle, hand_comparison, house_choice

    def __init__(self, mode: str = "STANDARD"):
        if mode == "STANDARD":
            deck_file = "standard_decks.json"

        with open(deck_file, "r") as payload:
            self.deck_list = json.load(payload)

        self.deck_1 = self.deck_list[0]
        self.deck_2 = self.deck_list[1]

        self.first_player = f"deck_{random.randint(1,2)}"
