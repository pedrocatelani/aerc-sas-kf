import csv

def get_id_deck() -> bool:
    
    with open("dok_decks.csv", mode="r", newline="", encoding="utf-8") as dok_decks:
        decks = csv.reader(dok_decks)
        
        next(decks)
        
        with open("dok_id.csv", "w") as dok_id:
            for deck_info in decks:
                dok_id.write(f'{deck_info[48][-36:]},\n')