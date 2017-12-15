class GeneticFunctions(object):
    """docstring for GeneticFunctions"""
    def probability_crossover(self):
        """return rate of occur corssover(0.0~1.0)."""
        return 0.75

    def probability_mutation(self):
        """return rate of occur mutation(0.0~1.0)."""
        return 0.02

    def initial(self):
        """return list of initial population."""
        return []

    def fitness(self, chromosome):
        """returns domain fitness value of chromosome."""
        return fitness

    def check_stop(self, fits_populations):
        """stop run if returns True.
        
        :param fits_populations: list of (fitness_value, chromsome) 
        """
        return False

    def parents(self, fits_populations):
        """generator of selected parents"""
        gen = list(sorted(fits_populations))
        while True:
            f1, ch1 = next(gen)
            f2, ch2 = next(gen)
            yield(ch1, ch2)
            pass
        return 

    def crossover(self, parents):
        """breed children"""
        return parents

    def mutation(self, chromosome):
        """mutate chromosome"""
        return chromosome
