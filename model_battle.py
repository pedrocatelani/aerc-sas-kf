import json
from battle_simulator import BattleSim


# Função utilitária (é uma arma secreta que utilizaremos no futuro!)
def get_attributes(deck: object):
    ae = 0
    ac = 0
    cc = 0
    cp = 0
    ep = 0
    dr = 0

    for syn in deck["synergies"]:
        ae += syn["expectedAmber"]
        ac += syn["amberControl"]
        cc += syn["creatureControl"]
        cp += syn["creatureProtection"]
        ep += syn["effectivePower"]
        dr += syn["disruption"]

    attributes = {
        "expectedAember": ae,
        "aemberControl": ac,
        "creatureControl": cc,
        "creatureProtection": cp,
        "effectivePower": ep,
        "disruption": dr,
    }

    return attributes


# Instanciando a classe que cuidará das batalhas
battle = BattleSim(mode="ALIANCE", rounds=101)


# Fetch do Deck modelo, gerado com base nos 901 alianças.
with open("model_deck.json", "r") as payload:
    model_deck = json.load(payload)


# Dicionário que guardará o número de vitórias
wins_dict = {}

# Loop de batalhas, onde, todos os decks lutam X vezes contra o deck modelo.
battles = 45
count = 1
for deck1 in range(0, len(battle.deck_list)):
    # Atribuição dos decks no objeto
    battle.deck_1 = battle.deck_list[deck1]
    battle.deck_2 = model_deck

    # Verificação, e criação das chaves no dicionário de vitórias
    if battle.deck_1["name"] not in wins_dict.keys():
        wins_dict[battle.deck_1["name"]] = [get_attributes(battle.deck_1), 0.0, 0]
    if battle.deck_2["name"] not in wins_dict.keys():
        wins_dict[battle.deck_2["name"]] = [get_attributes(model_deck), 0.0, 0]

    # Calculo dos vencedores
    wins = [0, 0]
    for i in range(0, battles + 1):
        wins1, wins2 = battle.battle()

        wins[0] += wins1
        wins[1] += wins2

    wins_dict[battle.deck_1["name"]][2] += wins[0]
    wins_dict[battle.deck_2["name"]][2] += wins[1]

    # Retorno para o console, em conjunto com o incremento da variável de controle
    print("Battle {} done".format(count))
    count += 1


# Calculando a winrate de cada deck, e adicionando a wins_dict
for k, v in wins_dict.items():
    wins_dict[k][1] = round((v[2] / battles) * 100, 4)

# Criando o Json de resultado, para análise
with open("model_result.json", "w") as payload:
    json.dump(wins_dict, payload)
