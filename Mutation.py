import random
from parameter import *


def mutation(particle_server, particle_order, inertia_weight):
    '''
    mutation operator:
    :param particle_server: old particle
    :param particle_order: old particle
    :param inertia_weight: inertia_weight
    :return: new particle
    '''
    r_1 = random.random()
    if r_1 < inertia_weight:
        # mutation location
        ind = random.randint(0, len(particle_server) - 1)
        # execution server mutation
        ori_ser = particle_server[ind]
        new_ser = random.randint(0, numberOfServer - 1)
        while new_ser == ori_ser:
            new_ser = random.randint(0, numberOfServer - 1)
        particle_server[ind] = new_ser
        # execution order mutation
        ori_ord = particle_order[ind]
        new_ord = random.randint(0, len(particle_server) - 1)
        while new_ord == ori_ord:
            new_ord = random.randint(0, len(particle_server) - 1)
        for i in range(len(particle_order)):
            if particle_order[i] == new_ord:
                particle_order[i] = ori_ord
        particle_order[ind] = new_ord
    return particle_server, particle_order
