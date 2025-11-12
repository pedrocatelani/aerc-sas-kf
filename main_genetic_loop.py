from genetic_algorithm import GeneticAlgorithm
from selection._roulette import Roulette

import numpy as np
from utils.plot_math import plot_fitness_evolution
from utils.plot_math import plot_attribute_comparison
# from selection._tournament import Tournament
# from selection._rankbased import RankBased


def main_genetic_loop(weight: dict = None, generations: int = 0, plot: list = []):
    # Instanciando a classe do GA
    w = {"ac": 2.12, "cc": 1.76, "cp": 13.3, "ep": 0.2612, "ea": 3.0, "dr": 1.5}
    gen = GeneticAlgorithm(w)
    print(gen.weight)
    
    # Armazenamento dos fitness
    fitness_history = []

    gen.create_deck_atr()
    print(">> Decks criados a partir do arquivo.")
    print(">> Tamanho da população: {}".format(len(gen.decks_atr)))

    gen.atr_normalization()
    print(">> População gerada a partir dos decks.")

    # A partir da população guardada no atributo norm_decks_atr,
    values = gen.evaluate()

    # Instanciando a classe de seleção (utilizando o método de seleção Roleta)
    # print(gen.values)
    
    fitness_history.append(np.mean(values))
    
    sel = Roulette(population=gen.values)

    next_progenitors = sel.select_n(len(gen.decks_atr), values)

    print("--------NextProgenitors")
    print(next_progenitors)
    print("-----------------------")

    index = 0
    descencendants = []
    while index < len(next_progenitors):
        name_1 = next_progenitors[index]["deck"]
        name_2 = next_progenitors[index + 1]["deck"]

        descencendants += [*gen.cross_shuffle(name_1, name_2)]

        index += 2
    # print(descencendants)

    # Loop principal
    ctrl = 0
    gen.build_descendants(descencendants, ctrl, first=True)
    while ctrl < generations:
        gen.create_deck_atr("ga_currentgen_decks.json")
        print(">> Decks criados a partir do arquivo.")
        print(">> Tamanho da população: {}".format(len(gen.decks_atr)))

        gen.atr_normalization()
        print(">> População gerada a partir dos decks.")

        values = gen.evaluate()
        
        fitness_history.append(np.mean(values))

        sel = Roulette(population=gen.values)

        next_progenitors = sel.select_n(len(gen.decks_atr), values)

        print("--------NextProgenitors GEN{}".format(ctrl))
        print(next_progenitors)
        print("-----------------------")

        index = 0
        descencendants = []
        while index < len(next_progenitors):
            name_1 = next_progenitors[index]["deck"]
            name_2 = next_progenitors[index + 1]["deck"]

            descencendants += [
                *gen.cross_shuffle(name_1, name_2, "ga_currentgen_decks.json")
            ]

            index += 2

        ctrl += 1
        gen.build_descendants(descencendants, ctrl, "ga_currentgen_decks.json")
        # input()
        
        if ctrl in plot:
            plot_fitness_evolution(fitness_history)        
            plot_attribute_comparison(gen.best_deck_atr_norm, gen.worst_deck_atr_norm, gen.best_deck_name, gen.worst_deck_name, gen.best_fitness_deck, gen.worst_fitness_deck)
    
    
    
