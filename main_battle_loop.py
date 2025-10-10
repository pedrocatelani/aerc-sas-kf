import json
from battle_simulator import BattleSim
from aliance import Aliance

def main_battle_loop(weight: dict = None):
    # Instância da classe Aliance, que constrói os decks do tipo Aliança
    # Configurada para o tipo Randômico
    aliance = Aliance("RANDOM")
    aliance.build()

    # Confirmação
    input("\n-- Enter para rodar com estes decks...")

    # Instância da classe BattleSim, responsável por simular as batalhas.
    # Configurada para o tipo Aliança, com pesos padrões, e quantidade de rodadas por deck igual a 20.
    battle = BattleSim(mode="ALIANCE", rounds=30, weight=weight)


    # Dicionário que guardará o número de vitórias
    wins_dict = {}

    # Loop de batalhas, onde, todos os decks lutam X vezes contra todos os outros decks.
    battles = 15
    count = 1
    for deck1 in range(0, len(battle.deck_list)):
        for deck2 in range(deck1 + 1, len(battle.deck_list)):

            # Atribuição dos decks no objeto
            battle.deck_1 = battle.deck_list[deck1]
            battle.deck_2 = battle.deck_list[deck2]

            # Verificação, e criação das chaves no dicionário de vitórias
            if battle.deck_1["name"] not in wins_dict.keys():
                wins_dict[battle.deck_1["name"]] = [0, 0.0]
            if battle.deck_2["name"] not in wins_dict.keys():
                wins_dict[battle.deck_2["name"]] = [0, 0.0]

            # Calculo dos vencedores
            wins = [0, 0]
            for i in range(0, battles + 1):
                wins1, wins2 = battle.battle()

                wins[0] += wins1
                wins[1] += wins2

            wins_dict[battle.deck_1["name"]][0] += wins[0]
            wins_dict[battle.deck_2["name"]][0] += wins[1]

            # Retorno para o console, em conjunto com o incremento da variável de controle
            print("Battle {} done".format(count))
            count += 1


    # Calculando a winrate de cada deck, e adicionando a wins_dict
    total_battles = (len(battle.deck_list) - 1) * battles
    for k, v in wins_dict.items():
        wins_dict[k][1] = round((v[0] / total_battles) * 100, 4)

    # Criando o Json de resultado, para análise
    with open("battle_result.json", "w") as payload:
        json.dump(wins_dict, payload)
