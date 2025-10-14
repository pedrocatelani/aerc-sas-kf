from numpy.random import random
from numpy import array, argsort

from . import Selection


class RankBased(Selection):
    def __init__(self, population):
        super(RankBased, self).__init__(population)

    def selecionar(self, fitness: array):
        rankings = argsort(fitness) + 1
        total = rankings.sum()

        stop = total * random()
        parcial = 0
        i = 0

        while True:
            if i > fitness.size - 1:
                break

            parcial += rankings[i]

            if parcial >= stop:
                break

            i += 1
        return i - 1
