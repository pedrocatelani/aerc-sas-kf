import json


class BattleSim:
    weight = {"ac": 2.12, "cc": 1.76, "cp": 13.3, "ep": 0.2612}

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

    player_1_disruption = 0
    player_2_disruption = 0

    deck_list = None
    rounds = 18

    from ._turn import (
        create_deck_pool,
        draw,
        create_card_values,
        discard_cards,
        get_chain,
    )
    from ._battle import battle, hand_comparison, house_choice, create_hand_strenght

    def set_pool_game(self, deck: int):
        if deck == 1:
            self.deck_1_pool_game = self.deck_1_pool.copy()
        if deck == 2:
            self.deck_2_pool_game = self.deck_2_pool.copy()

    def __init__(self, weight: dict = None, mode: str = "STANDARD", rounds: int = None):
        """
        "weight" param must contain: {ac, cc, cp, ep} as keys.\n
        "mode" param can be "STANDARD" or "ALIANCE".\n
        "rounds" param sets the amount of rounds per battle.
        """

        if mode == "STANDARD":
            deck_file = "standard_decks.json"
        elif mode == "ALIANCE":
            deck_file = "aliance_decks.json"
        if weight:
            self.weight = weight
        if rounds:
            self.rounds = rounds

        with open(deck_file, "r") as payload:
            self.deck_list = json.load(payload)

        self.deck_1 = self.deck_list[0]
        self.deck_2 = self.deck_list[1]
