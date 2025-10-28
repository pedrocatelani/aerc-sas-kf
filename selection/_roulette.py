from numpy.random import random
from numpy import array

from . import Selection


class Roulette(Selection):
    def __init__(self, population: list):
        super(Roulette, self).__init__(population)

    def select(self, fitness: array):
        fmin = fitness.min()
        adjusted_fitness = fitness - fmin

        # print(f"Fitness Ajustado (F - Fmin): {adjusted_fitness}")

        total = adjusted_fitness.sum()

        stop = total * (1.0 - random())
        parcial = 0
        i = 0

        # print("total", total)
        # print("parcial", parcial)
        # print("stop", stop)

        while True:
            if i > fitness.size - 1:
                break

            parcial += fitness[i]

            if parcial >= stop:
                break

            i += 1

        return i
