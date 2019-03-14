import random
import numpy as np
import argparse


def check_parameters_execute_pso():
    try:

        if num_of_iterations <= 0 or num_of_particles <= 0:
            raise Exception("Input parameters has to be positive!")

        if value_of_w > 1 or value_of_w < -1:
            raise Exception("Inertia coefficient has to be in [-1,1]")

        c1_c2 = [value_of_c1, value_of_c2]
        sum_of_c1_c2 = sum(c1_c2)
        if sum_of_c1_c2 > 4.4 or sum_of_c1_c2 < 0.1:
            raise Exception("The sum of cognitive and social coefficient has to be in [0.1,4.4]")

        execute_pso()

    except Exception as e:
        print("Invalid input parameters. " + str(e))


def execute_pso():

    search_in_pso = PSO(0, target_error, num_of_particles)
    particles_vector = [Particle() for _ in range(search_in_pso.num_of_particles)]
    search_in_pso.particles = particles_vector

    i = 0
    while i < num_of_iterations:
        search_in_pso.set_pbest()
        search_in_pso.set_gbest()

        if abs(search_in_pso.gbest_value - search_in_pso.target) <= search_in_pso.target_error:
            break

        search_in_pso.search_iteration()
        i += 1

    print("The user entered %d as number of iterations, %d as number of particles, %f as inertia weight, "
          "%f as personal acceleration coefficient and %f as social acceleration coefficient" % (
          num_of_iterations, num_of_particles, value_of_w, value_of_c1, value_of_c2))
    print("The global best solution is: %s, this is achieved at iteration %s" % (search_in_pso.gbest_position, i))

    return search_in_pso.gbest_position


class Particle:
    # initialize properties of particle including current position,
    # global best, local best and velocity
    def __init__(self):
        # default constructor
        # initialize random positive and negative numbers of x and y in range (-15,15)
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 15,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 15])
        self.pbest_p = self.position
        self.pbest_v = float('inf')
        self.velocity = np.array([0, 0])

    # the next position of the particle is current position + its velocity
    # more precisely its a displacement
    def update_postition(self):
        self.position = self.position + self.velocity


class PSO:
    # parameterized constructor

    def __init__(self, target, target_error, num_of_particles):
        self.target = target
        self.target_error = target_error
        self.num_of_particles = num_of_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random() * 15, random.random() * 15])

    # The formula of Ackley function from wikipedia
    # this is Ackley function in its 2 dimensional domain
    def ackley(self, x):
        p1 = (-20) * np.exp((-0.2) * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2)))
        p2 = np.exp(0.5 * (np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1])))
        result = p1 - p2 + np.e + 20
        return result

    # set the local best value
    # the function value less than local best
    # update function value as local best
    def set_pbest(self):
        for particle in self.particles:
            fitness_value = self.ackley(particle.position)
            if particle.pbest_v > fitness_value:
                particle.pbest_v = fitness_value
                particle.pbest_p = particle.position

    # set the global best value
    # if the function value is less than global best
    # update function value as global best
    def set_gbest(self):
        for particle in self.particles:
            best_fitness_value = self.ackley(particle.position)
            if self.gbest_value > best_fitness_value:
                self.gbest_value = best_fitness_value
                self.gbest_position = particle.position

    # search through all iterations
    # update velocity of the next particle
    # update the position of the next particle
    def search_iteration(self):
        for particle in self.particles:
            new_velocity = (value_of_w * particle.velocity) + (value_of_c1 * random.random()) * (
                        particle.pbest_p - particle.position) + \
                           (random.random() * value_of_c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.update_postition()


# main function to execute iterations
if __name__ == "__main__":
    # user to enter number of iterations, particles, inertia weight w, acceleration coefficient c1 and c2
    # when there are 5 arguments, proceed
    # number of iterations, number of particles, inertia weight,
    # personal and social acceleration coefficient are the input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("num_iteration", type=int, help="number of iteration")
    parser.add_argument("num_particle", type=int, help="number of particles")
    parser.add_argument("w", type=float, help="value of w")
    parser.add_argument("c1", type=float, help="value of c1")
    parser.add_argument("c2", type=float, help="value of c2")
    parser.add_argument("error", type=float, help="value of target error")

    args = parser.parse_args()

    num_of_iterations = args.num_iteration
    num_of_particles = args.num_particle
    value_of_w = args.w
    value_of_c1 = args.c1
    value_of_c2 = args.c2
    target_error = args.error

    check_parameters_execute_pso()




