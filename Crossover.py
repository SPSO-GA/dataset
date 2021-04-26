import random
from parameter import *


def crossover(particle_server, particle_order, particle_server_best, particle_order_best, c):
    r = random.random()
    if r < c:
        res = random.sample(range(0, len(particle_server)), 2)
        ind1 = res[0]
        ind2 = res[1]
        if ind1 > ind2:
            ind1, ind2 = ind2, ind1
        particle_server[ind1:ind2 + 1] = particle_server_best[ind1: ind2 + 1]
        for i in range(len(particle_order[ind1:ind2 + 1])):
            for j in range(len(particle_order)):
                if particle_order_best[ind1:ind2 + 1][i] == particle_order[j]:
                    particle_order[j] = particle_order[ind1:ind2 + 1][i]
                    break
        particle_order[ind1:ind2 + 1] = particle_order_best[ind1:ind2 + 1]
    return particle_server, particle_order
