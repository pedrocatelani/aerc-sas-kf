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
    
def draw(self):
    while len(self.player_1_hand) < 6:
        card = rd.choice(self.deck_1_pool_game)
        self.player_1_hand.append(card)
        self.deck_1_pool_game.remove(card)
    
    while len(self.player_2_hand) < 6:
        card = rd.choice(self.deck_2_pool_game)
        self.player_2_hand.append(card)
        self.deck_2_pool_game.remove(card)
    

    