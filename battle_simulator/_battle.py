def battle(self):
    round = 1
    self.create_deck_pool()
    self.create_card_values()

    self.draw(1)
    self.draw(2)

    self.hand_comparison()
    
def hand_comparison(self):
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
            
    #(Cprotec > CCtrl), (CCtrl > EPower),  (EPower > Actrl),  (Actrl > EAmber)
    

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
