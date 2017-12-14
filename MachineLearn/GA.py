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


distribute_times = [[46,62,123,191,130,83,144,207,215,153,105,161,227],
                    [114,120,180,139,196,149,204,144,151,212,162,226,168],
                    [166,179,127,72,131,206,145,89,99,156,227,162,108],
                    [54,70,127,200,141,91,149,209,221,155,114,173,230],
                    [113,129,186,137,195,145,209,154,164,215,174,229,166],
                    [174,185,131,80,136,210,154,88,101,158,228,169,112]]

mareas = [240,300,270,270,300,240]
sareas = [24,22,26,33,5,5,5,5,19,41,18,31,24]


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
        flag = 1 
        transfers = get_transfers(chromo)
        flag = judge_over_area(transfers)
        for transfer in transfers:
            if transfer.arrival_time == 0:
                flag = 0
                break
            drive_time += transfer.drive_time
        
        fitness = drive_time + 100000*(1-flag)
        return fitness


    # internals
    def random_chromo(self,stash_num,market_num,veh_num):
        chromo = []
        for i in range(stash_num):
            cor_veh = random.randrange(veh_num)
            cor_market = random.randrange(market_num)
            chromo.append([cor_veh,cor_market])
        return chromo


def get_transfers(chromo):
    chromo_size = len(chromo)
    transfers = []
    for stash_num in range(chromo_size):
        prev_transfer = None
        if stash_num == 0 :
            car_num = chromo[stash_num][0]
            market_num = chromo[stash_num][1]
            cur_transfer = Transfer(car_num,stash_num,market_num)
            transfers.append(cur_transfer)
        else:
            car_num = chromo[stash_num][0]
            market_num = chromo[stash_num][1]
            for transfer in transfers:
                if transfer.car.car_num == car_num:
                    prev_transfer = transfer
            cur_transfer = Transfer(car_num,stash_num,market_num,prev_transfer)
            transfers.append(cur_transfer)
    return transfers

def judge_over_area(transfers):
    flag = 1
    area_couples = {}
    for transfer in transfers:
        market_num = transfer.departure.market_num
        if not market_num in area_couple:
            area_couples[market_num] = [transfer]
        else:
            area_couples[market_num].append(transfer)

    for market_num in area_couples:
        total_area = 0
        com_transfers = area_couples[market_num]
        com_market = Market(market_num)
        for transfer in com_transfers:
            stash_area = transfer.destination.stash_area
            total_area += 5*stash_area
        if total_area > com_market.market_area:
            flag = 0
    return flag
    


class Transfer(object):
    """docstring for Transfer"""
    def __init__(self,car_num,stash_num,market_num,prev_transfer = None):
        self.car = Car(car_num)
        self.departure = Market(market_num)
        self.destination = Stash(stash_num)
        self.prev_transfer = prev_transfer
        self.drive_time = self.get_drive_time()
        self.arrival_time = self.get_arrival_time()
    
    def get_expected_time(self):
        if not self.prev_transfer:
            expected_time = distribute_times[self.departure.market_num][self.destination.stash_num]
        else:
            prev_stash = self.prev_transfer.destination
            expected_time = self.prev_transfer.arrival_time + distribute_times[self.departure.market_num][prev_stash.stash_num] \
            + distribute_times[self.departure.market_num][self.destination.stash_num]
        return expected_time

    def get_arrival_time(self):
        expected_time = self.get_expected_time()
        max_arrival_time = (self.destination.stash_num + 1) * 2 * 60
        min_arrival_time = self.destination.stash_num * 2 * 60
        if expected_time > max_arrival_time:
            arrival_time = 0
        elif expected_time < min_arrival_time:
            arrival_time = min_arrival_time
        else:
            arrival_time = expected_time
        return arrival_time

    def get_drive_time(self):
        if not self.prev_transfer:
            drive_time = distribute_times[self.departure.market_num][self.destination.stash_num]
        else:
            prev_stash = self.prev_transfer.destination
            drive_time = distribute_times[self.departure.market_num][prev_stash.stash_num] \
            + distribute_times[self.departure.market_num][self.destination.stash_num]
        return drive_time


class Car(object):
    def __init__(self,car_num):
        self.car_num = car_num


class Market(object):
    """docstring for Market"""
    def __init__(self,market_num):
        self.market_num = market_num
        self.market_area = mareas[market_num]


class Stash(object):
    def __init__(self,stash_num):
        self.stash_num = stash_num
        self.stash_area = sareas[stash_num]
        

if __name__ == '__main__':
    """solve logistics distribution problem"""
    # logi = Logistics()
    # populations = logi.initial(13,6,3)
    # fits_pops = [(logi.fitness(chromo), chromo) for chromo in populations]
    # print(fits_pops)
    chromo_demo = [[0,0],[0,3],[1,1],[2,5],[2,2],[0,0],[2,2],[1,5],[1,2],[0,4],[2,0],[0,3],[1,2]]
    transfers = get_transfers(chromo_demo)
    for transfer in transfers:
        print(transfer.arrival_time)
    for transfer in transfers:
        print(transfer.car.car_num,':',transfer.drive_time)
    

        