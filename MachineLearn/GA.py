"""Problem:
以工位为中心的生产物流配送优化，
求解总配送时间最小时，k辆配送工具的配送路线和“工位组-物料点”的对应关系。
"""

"""实例
89个工位（13组），6个物料点。一个工作日配送循环次数N=5，生产节拍为2min。 

"""

import pdb
import random


class GeneticAlgorithm(object):
    def __init__(self, genetics):
        pass

    def run(self):
        population = self.genetics.initial()
        while True:
            fits_pops = [(self.genetics.fitness(chromo), chromo) for chromo in population]
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

class Center(object):
    """docstring for Center"""
    time_windows = [2,4,6,8,10,12,14,16,18,20,22,24]

    def __init__(self, arg):
        pass


distribute_times = [[46,62,123,191,130,83,144,207,215,153,105,161,227],
                    [114,120,180,139,196,149,204,144,151,212,162,226,168],
                    [166,179,127,72,131,206,145,89,99,156,114,173,230],
                    [54,70,127,200,141,91,149,209,221,155,114,173,230],
                    [113,129,186,137,195,145,209,154,164,215,174,229,166],
                    [174,185,131,80,136,210,154,88,101,158,228,169,112]]

market_area = [240,300,270,270,300,240]
stash_area = [24,22,26,33,5,5,5,5,19,41,18,31,24]

class Stash(object):
    
    def __init__(self,stash_index,time_window,resource_area):
        self.stash_index = stash_index
        self.time_window = time_window
        self.resource_area = resource_area

    def stash_market_time(mindex):
        return distribute_times[self.stash_index][mindex]
                  
class Market(object):
    
    def __init__(self,market_index,market_area):
        self.market_index = market_index
        self.market_area = market_area

    def market_stash_time(sindex):
        return distribute_times[self.market_index][sindex]


class Logistics(GeneticFunctions):
    """docstring for logistics"""
    def __init__(self,generations=50,size=100,prob_crossover=0.75,prob_mutation=0.3):
        self.counter = 0

        self.generations = generations
        self.size = size
        self.prob_crossover = prob_crossover
        self.prob_mutation = prob_mutation

    def probability_crossover(self):
        return self.prob_crossover

    def probability_mutation(self):
        return self.prob_mutation

    def initial(self,stash_num,market_num,veh_num):
        return [self.random_chromo(stash_num,market_num,veh_num)]

    def fitness(self, chromo):
        #计算适应度,适应度计算的规则为每条配送路径要满足题设条件，并且目标函数即车辆行驶的时间越少，适应度越高
        stash_num = len(chromo)
        vehi_fit = 0
        mar2sta_fit = 0
        vehi_couple = {}
        market_stash = {}
        for i in range(stash_num):
            vehi_index = chromo[i][0]
            if not vehi_index in vehi_couple:
                vehi_couple[vehi_index] = []
                vehi_couple[vehi_index].append([chromo[i],i])
            else:
                vehi_couple[vehi_index].append([chromo[i],i])
            market_index = chromo[i][1]
            if not market_index in market_stash:
                market_stash[market_index] = []
                market_stash[market_index].append([chromo[i],i])
            else:
                market_stash[market_index].append([chromo[i],i])
            time_mar2sta = distribute_times[market_index-1][i]
            vehi_fit += time_mar2sta
        print(vehi_couple)
        for vehi_index in vehi_couple:
            target = vehi_couple.get(vehi_index)
            for j in range(len(target)-1):
                chromo_part_prev = target[j]
                chromo_part_next = target[j+1]
                stash_index_prev = chromo_part_prev[1]
                market_index_next = chromo_part_next[0][1]
                time_sta2mar = distribute_times[market_index_next-1][stash_index_prev]
                mar2sta_fit += time_sta2mar
        # if self.time_area_restrit(vehi_couple,market_stash):
        #     flag = 0
        # else:
        #     flag = 1
        fitness = mar2sta_fit + vehi_fit
        return fitness


    # internals
    def random_chromo(self,stash_num,market_num,veh_num):
        chromo = []
        for i in range(stash_num):
            cor_veh = random.randint(1,veh_num)
            cor_market = random.randint(1,market_num)
            chromo.append([cor_veh,cor_market])
        return chromo

    def time_area_restrit(self,vehi_couple,market_stash):
        for market_index in market_stash:
            total_stasharea = 0
            cor_stashs = market_stash[market_index]
            for i in range(len(cor_stashs)):
                cor_stashindex = cor_stashs[i]
                cor_stasharea = stash_area[cor_stashindex]
                total_stasharea += 5 * cor_stasharea
            if total_stasharea > market_area[market_index-1]:
                return False

        for vehi_index in vehi_couple:
            arrival_time = 0
            chromos = vehi_couple[vehi_index]
            for i in range(len(chromos)):
                if i == 0 :
                    cor_stashindex += chromos[i][1]
                    arrival_time += distribute_times[vehi_index-1][cor_stashindex]
                    pass


if __name__ == '__main__':
    """solve logistics distribution problem"""
    logi = Logistics()
    populations = logi.initial(13,6,3)
    fits_pops = [(logi.fitness(chromo), chromo) for chromo in populations]
    print(fits_pops)
    

        