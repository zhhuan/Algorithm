"""Problem:
以工位为中心的生产物流配送优化，
求解总配送时间最小时，k辆配送工具的配送路线和“工位组-物料点”的对应关系。
"""

"""实例
89个工位（13组），6个物料点。一个工作日配送循环次数N=5，生产节拍为2min。 

"""

class GeneticAlgorithm(object):
    def __init__(self, genetics):
        pass

    def run(self):
        population = self.genetics.initial()
        while True:
            fits_pops = [(self.genetics.fitness(chrom), chrom) for chrom in population]
            if self.genetics.check_stop(fits_pops):
                break
            population = self.next(fits_pops)
            pass
        return population

    def next(self, fits):
        parents_generator = self.genetics.parents(fits)
        size = len(fits)
        nexts = []
        while len(nexts) < size:
            parents = next(parents_generator)
            cross = random.random() < self.genetics.probability_crossover()
            children = self.genetics.crossover(parents) if cross else parents  #小于交叉概率，做交叉
            for chrom in children:
                mutate = random.random() < self.genetics.probability_muttation()
                nexts.append(self.genetics.mutation(chrom) if mutate else ch)
                pass
            pass
        return nexts[0:size]


class GeneticFunctions(object):
    """docstring for GeneticFunctions"""
    def __init__(self, arg):
        super(GeneticFunctions, self).__init__()
        self.arg = arg

    def probability_crossover(self):
        """return rate of occur corssover(0.0~1.0)"""
        return 0.75

    def probability_mutation(self):
        """return rate of occur mutation(0.0~1.0)"""
        return 0.02

    def fitness(self, chromosome):
        """returns domain fitness value of chromosome."""
        return fitness

    def crossover(self, parents):
        """breed children"""
        return parents

    def mutation(self, chromosome):
        """mutate chromosome"""
        return chromosome


        