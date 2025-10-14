from numpy.random import choice
from numpy import array, where
from . import Selection


class Tournament(Selection):
    def __init__(self, population, size=10):
        super(Tournament, self).__init__(population)
        self.size = size

    def selecionar(self, fitness: array):
        individuals = choice(fitness, size=self.size)
        champion = individuals.max()
        i = where(fitness == champion)[0][0]

        return i
