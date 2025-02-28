import random as rd


def create_deck_pool(self):
    pool_1 = []
    pool_2 = []
    for house in self.deck_1["houses"]:
        pool_1 = [*pool_1, *house["cards"]]
    for house in self.deck_2["houses"]:
        pool_2 = [*pool_2, *house["cards"]]

    self.deck_1_pool = pool_1.copy()
    self.deck_2_pool = pool_2.copy()
    self.deck_1_pool_game = pool_1.copy()
    self.deck_2_pool_game = pool_2.copy()
    self.player_1_hand = []
    self.player_2_hand = []


def draw(self, deck, max: int = 6):
    hand = getattr(self, f"player_{deck}_hand")
    pool_game = getattr(self, f"deck_{deck}_pool_game")

    while len(hand) < max:
        if len(pool_game) <= 0:
            self.set_pool_game(deck)
            pool_game = getattr(self, f"deck_{deck}_pool_game")

        card = rd.choice(pool_game)
        hand.append(card)
        pool_game.remove(card)

    if max != 6:
        if deck == 1:
            self.player_1_disruption -= 1
        if deck == 2:
            self.player_2_disruption -= 2


def discard_cards(self, house: str, deck: int):
    hand = getattr(self, f"player_{deck}_hand")
    indexes = []
    for i in range(0, len(hand)):
        if hand[i][0] == house:
            indexes.append(i)

    indexes.sort(reverse=True)
    for i in indexes:
        hand.pop(i)


def get_chain(self, deck: int):
    disruption = getattr(self, f"player_{deck}_disruption")
    chain_list = [
        [19, 2],
        [13, 3],
        [7, 4],
        [1, 5],
        [-99999, 6],
    ]
    for i in chain_list:
        if disruption >= i[0]:
            return i[1]


def create_card_values(self):
    values = {}
    for house in self.deck_1["houses"]:
        ea = 0
        ac = 0
        cc = 0
        ep = 0
        cp = 0
        dr = 0
        name = house["name"]
        for syn in self.deck_1["synergies"]:
            if syn["house"] == name:
                ea += syn["expectedAmber"]
                ac += syn["amberControl"]
                cc += syn["creatureControl"]
                ep += syn["effectivePower"]
                cp += syn["creatureProtection"]
                dr += syn["disruption"]
        values[name] = {
            "house": name,
            "expectedAmber": (ea / 12) * 1,
            "amberControl": (ac / 12) * self.weight["ac"],
            "creatureControl": (cc / 12) * self.weight["cc"],
            "effectivePower": (ep / 12) * self.weight["ep"],
            "creatureProtection": (cp / 12) * self.weight["cp"],
            "disruption": (dr / 12) * 1,
        }

    self.deck_1_values = values.copy()

    values = {}
    for house in self.deck_2["houses"]:
        ea = 0
        ac = 0
        cc = 0
        ep = 0
        cp = 0
        dr = 0
        name = house["name"]
        for syn in self.deck_2["synergies"]:
            if syn["house"] == name:
                ea += syn["expectedAmber"]
                ac += syn["amberControl"]
                cc += syn["creatureControl"]
                ep += syn["effectivePower"]
                cp += syn["creatureProtection"]
                dr += syn["disruption"]
        values[name] = {
            "house": name,
            "expectedAmber": (ea / 12) * 1,
            "amberControl": (ac / 12) * self.weight["ac"],
            "creatureControl": (cc / 12) * self.weight["cc"],
            "effectivePower": (ep / 12) * self.weight["ep"],
            "creatureProtection": (cp / 12) * self.weight["cp"],
            "disruption": (dr / 12) * 1,
        }

    self.deck_2_values = values.copy()
