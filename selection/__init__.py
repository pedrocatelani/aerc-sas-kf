from numpy import array


# Classe Abstrata de seleções
class Selection:
    def __init__(self, population: list):
        self.population = array(population)

    def select(self, fitness):
        """
        return indexes of selected individuals
        """
        raise NotImplementedError("Not yet implemented")

    def select_n(self, n: int, fitness=None):
        """
        return 'n' selected individuals
        """
        progenitors = array([self.select(fitness) for _ in range(n)])

        print(progenitors)
        return self.population[progenitors]
