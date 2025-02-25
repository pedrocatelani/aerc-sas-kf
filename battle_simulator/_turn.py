import random as rd


def create_deck_pool(self):
    pool_1 = []
    pool_2 = []
    for house in self.deck_1["houses"]:
        pool_1 = [*pool_1, *house["cards"]]
    for house in self.deck_2["houses"]:
        pool_2 = [*pool_2, *house["cards"]]

    self.deck_1_pool = pool_1
    self.deck_2_pool = pool_2
    self.deck_1_pool_game = pool_1
    self.deck_2_pool_game = pool_2


def draw(self, deck, max: int = 6):
    hand = getattr(self, f"player_{deck}_hand")
    pool_game = getattr(self, f"deck_{deck}_pool_game")

    while len(hand) < max:
        card = rd.choice(pool_game)
        hand.append(card)
        pool_game.remove(card)


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
            "expectedAmber": ea / 12,
            "amberControl": ac / 12,
            "creatureControl": cc / 12,
            "effectivePower": ep / 12,
            "creatureProtection": cp / 12,
            "disruption": dr / 12,
        }

    self.deck_1_values = values

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
            "expectedAmber": ea / 12,
            "amberControl": ac / 12,
            "creatureControl": cc / 12,
            "effectivePower": ep / 12,
            "creatureProtection": cp / 12,
            "disruption": dr / 12,
        }
        
    self.deck_2_values = values
