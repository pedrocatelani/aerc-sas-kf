import json


class Aliance:

    standard_decks = None
    aliance_decks = None
    mode = None
    selected_decks_keys = []
    selected_decks = []

    from ._builder import build, build_sequential, build_random, create, create_name

    def __init__(self, mode: str = "SEQUENTIAL"):
        """
        "mode" param can be "SEQUENTIAl" or "RANDOM".
        """
        
        self.mode = mode
        deck_file = "standard_decks.json"

        with open(deck_file, "r") as payload:
            self.standard_decks = json.load(payload)
