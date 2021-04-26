from parameter import *
from Particle2EnergyCons import particle2energy
import random


def SPSOGA(Task):
    # 初始化粒子群
    particle_swarm_server = []
    particle_swarm_order = []
    for i in range(numberOfParticle):
        particle_server = []
        particle_order = []
        for j in range(len(Task.subTask)):
            particle_server.append(random.randint(0, numberOfServer - 1))
            particle_order.append(j)
        random.shuffle(particle_order)
        particle_swarm_server.append(particle_server)
        particle_swarm_order.append(particle_order)
    # 初始化pbest
    pbest_particles_server = particle_swarm_server
    pbest_particles_order = particle_swarm_order
    # 初始化gbest
    gbest_paticle_server = []
    gbest_paticle_order = []
    gbest_energy_cons = 9999999
    for i in range(len(pbest_particles_server)):
        energy_cons = particle2energy(Task, pbest_particles_server[i], pbest_particles_order[i])
        if energy_cons < gbest_energy_cons:
            gbest_energy_cons = energy_cons
            gbest_paticle_server = pbest_particles_server[i]
            gbest_paticle_order = pbest_particles_order[i]
