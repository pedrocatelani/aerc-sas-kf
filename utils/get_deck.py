import requests as re
import csv
from configparser import ConfigParser
from time import sleep

from utils.json_convert import add_dec
from utils.counter import aerc_count


def get_deck() -> bool:
    settings = ConfigParser()
    settings.read("config.ini")
    data = []
    try:
        with open("id.csv", mode="r", newline="") as id_file:
            print(">> Iniciando Fetch da api...")
            ids = csv.reader(id_file)
            i = 1

            for deck_id in ids:
                print("Deck {} --> {}".format(i,deck_id[0]))
                url = f"https://decksofkeyforge.com/public-api/v3/decks/{deck_id[0]}"
                header = {"Api-Key": settings["USER"]["api_key"]}

                response = re.get(url=url, headers=header)
                if response.status_code == 200:
                    deck = response.json()
                    data.append(deck["deck"])
                else:
                    print(response)
                    print("!> Processo encerrado forçadamente")
                    print("!> Verifique sua chave de API, e tente novamente.")
                    return False

                sleep(2)
                i += 1

            print("\n>> Processo finalizado.\n")
            add_dec(data)
            aerc_count(data)
            return True
    except:
        print("!> Verifique seu arquivo 'id.csv', e tente novamente.")
        return False