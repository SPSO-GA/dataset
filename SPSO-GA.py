from parameter import *
from Particle2EnergyCons import particle2energy
from Mutation import mutation
from Crossover import crossover
import random


def SPSOGA(Task):
    # Initial popution
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
    # Initial pbest
    pbest_particles_server = particle_swarm_server
    pbest_particles_order = particle_swarm_order
    pbest_energy_cons = []
    for i in range(numberOfParticle):
        pbest_energy_cons.append(particle2energy(Task, pbest_particles_server[i], pbest_particles_order[i]))
    # Initial gbest
    gbest_paticle_server = []
    gbest_paticle_order = []
    gbest_energy_cons = 9999999
    for i in range(len(pbest_particles_server)):
        energy_cons = particle2energy(Task, pbest_particles_server[i], pbest_particles_order[i])
        if energy_cons < gbest_energy_cons:
            gbest_energy_cons = energy_cons
            gbest_paticle_server = pbest_particles_server[i]
            gbest_paticle_order = pbest_particles_order[i]

    for i in range(iterations_max):
        # inertia weight
        w = 0.5
        for j in range(numberOfParticle):
            # inertia
            particle_swarm_server[j], particle_swarm_order[j] = mutation(particle_swarm_server[j],
                                                                         particle_swarm_order[j], w)
            # personal cognition
            c_1 = random.random()
            particle_swarm_server[j], particle_swarm_order[j] = crossover(particle_swarm_server[j],
                                                                          particle_swarm_order[j],
                                                                          pbest_particles_server[j],
                                                                          pbest_particles_order[j], c_1)
            # social cognition
            c_2 = random.random()
            particle_swarm_server[j], particle_swarm_order[j] = crossover(particle_swarm_server[j],
                                                                          particle_swarm_order[j],
                                                                          gbest_paticle_server,
                                                                          gbest_paticle_order, c_2)
            # update pbest
            energy_cons = particle2energy(Task, pbest_particles_server[j], pbest_particles_order[j])
            if energy_cons < pbest_energy_cons[j]:
                pbest_energy_cons[j] = energy_cons
                pbest_particles_server = pbest_particles_server[j]
                pbest_particles_order = pbest_particles_order[j]
                # update gbest
                if energy_cons < gbest_energy_cons:
                    gbest_energy_cons = energy_cons
                    gbest_paticle_server = pbest_particles_server[j]
                    gbest_paticle_order = pbest_particles_order[j]
    return gbest_energy_cons
