import json

def add_dec(data):
    
    with open("decks.json", "w") as payload:
            json.dump(data, payload)