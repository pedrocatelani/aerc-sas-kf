import requests as re
import csv
from configparser import ConfigParser
from time import sleep
from utils.json_convert import add_dec
from utils.counter import aerc_count


settings = ConfigParser()
settings.read('config.ini')
data = []
with open("id.csv", mode="r", newline="") as id_file:
    ids = csv.reader(id_file)

    for deck_id in ids:
        print(deck_id[0])
        url = f"https://decksofkeyforge.com/public-api/v3/decks/{deck_id[0]}"
        header = {"Api-Key": settings["USER"]["api_key"]}

        response = re.get(url=url, headers=header)
        if response.status_code == 200:
            deck = response.json()
            data.append(deck["deck"])
        else:
            print(response)

        sleep(3)

    add_dec(data)
    aerc_count(data)
