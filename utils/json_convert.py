import json

def add_dec(data):
    
    with open("api_decks.json", "w") as payload:
            json.dump(data, payload)