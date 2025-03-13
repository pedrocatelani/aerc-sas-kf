def battle(self):
    points = [0, 0]
    self.create_card_values()
    self.create_deck_pool()

    for i in range(0, self.rounds):
        self.draw(1, self.get_chain(1))
        self.draw(2, self.get_chain(2))

        p1, p2 = self.hand_comparison()
        points[0] += p1
        points[1] += p2

    if p1 > p2:
        return (1, 0)
    elif p2 > p1:
        return (0, 1)
    else:
        return (1, 1)


def hand_comparison(self) -> tuple:
    str_1, str_2 = self.create_hand_strenght()

    results_1 = [
        str_1["amberControl"] + str_1["creatureProtection"] - str_2["creatureControl"],
        str_1["creatureControl"] - str_2["creatureProtection"],
        str_1["effectivePower"]
        + str_1["creatureProtection"]
        - str_2["effectivePower"]
        - str_2["creatureProtection"],
    ]
    results_2 = [
        str_2["amberControl"] + str_2["creatureProtection"] - str_1["creatureControl"],
        str_2["creatureControl"] - str_1["creatureProtection"],
        str_2["effectivePower"]
        + str_2["creatureProtection"]
        - str_1["effectivePower"]
        - str_1["creatureProtection"],
    ]
    points_1 = 0
    points_2 = 0
    # print(results_1, results_2)
    # print(str_1["expectedAmber"], str_2["expectedAmber"])

    for i in range(0, 3):
        if results_1[i] > str_2["expectedAmber"]:
            points_1 += 1
        else:
            points_2 += 1

        if results_2[i] > str_1["expectedAmber"]:
            points_2 += 1
        else:
            points_1 += 1

    return (points_1, points_2)


def house_choice(self, deck):
    hand = getattr(self, f"player_{deck}_hand")
    aux = {}
    for card in hand:
        house = card[0]
        if house in aux:
            aux[house] += 1
        else:
            aux[house] = 1

    return max(aux, key=aux.get)


def create_hand_strenght(self) -> tuple:
    str_1 = {
        "expectedAmber": 0.0,
        "amberControl": 0.0,
        "creatureControl": 0.0,
        "effectivePower": 0.0,
        "creatureProtection": 0.0,
    }
    str_2 = {
        "expectedAmber": 0.0,
        "amberControl": 0.0,
        "creatureControl": 0.0,
        "effectivePower": 0.0,
        "creatureProtection": 0.0,
    }
    p_1 = self.house_choice(1)
    p_2 = self.house_choice(2)
    for card in self.player_1_hand:
        if card[0] == p_1:
            str_1["expectedAmber"] += self.deck_1_values[p_1]["expectedAmber"]
            str_1["amberControl"] += self.deck_1_values[p_1]["amberControl"]
            str_1["creatureControl"] += self.deck_1_values[p_1]["creatureControl"]
            str_1["effectivePower"] += self.deck_1_values[p_1]["effectivePower"]
            str_1["creatureProtection"] += self.deck_1_values[p_1]["creatureProtection"]
            self.player_2_disruption += self.deck_1_values[p_1]["disruption"]

    for card in self.player_2_hand:
        if card[0] == p_2:
            str_2["expectedAmber"] += self.deck_2_values[p_2]["expectedAmber"]
            str_2["amberControl"] += self.deck_2_values[p_2]["amberControl"]
            str_2["creatureControl"] += self.deck_2_values[p_2]["creatureControl"]
            str_2["effectivePower"] += self.deck_2_values[p_2]["effectivePower"]
            str_2["creatureProtection"] += self.deck_2_values[p_2]["creatureProtection"]
            self.player_1_disruption += self.deck_2_values[p_2]["disruption"]

    self.discard_cards(p_1, 1)
    self.discard_cards(p_2, 2)

    return (str_1, str_2)
