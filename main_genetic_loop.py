import numpy


from genetic_algorithm import GeneticAlgorithm
from selection._roulette import Roulette
from selection._tournament import Tournament
from selection._rankbased import RankBased


def main_genetic_loop(weight: dict = None):
    # Instanciando a classe do GA
    w = {"ac": 2.12, "cc": 1.76, "cp": 13.3, "ep": 0.2612, "ea": 3.0, "dr": 1.5}
    gen = GeneticAlgorithm(w)
    print(gen.weight)

    gen.create_deck_atr()
    print(">> Decks criados a partir do arquivo.")

    gen.atr_normalization()
    print(">> População gerada a partir dos decks.")

    # A partir da população guardada no atributo norm_decks_atr,
    values = gen.evaluate()

    # Instanciando a classe de seleção (utilizando o método de seleção Roleta)
    print(gen.values)
    sel = Roulette(population=gen.values)

    next_progenitors = sel.select_n(27, values)

    print(next_progenitors)
