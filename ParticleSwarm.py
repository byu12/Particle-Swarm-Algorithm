import random
import numpy as np
import argparse
import sys
import csv
from cookiecutter.main import cookiecutter


def parse_arguments(arg):

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

    arguments = parser.parse_args(arg)

    return arguments


def check_parameters_execute_pso():
    try:
        message = "Invalid input parameters. "
        # number of iterations and particles can not be negative
        if num_of_iterations <= 0:
            raise Exception("Input parameter number of iteration has to be positive!")

        # number of particles can not be negative
        if num_of_particles <= 0:
            raise Exception("Input parameter number of particles has to be positive!")

        # value of inertia weight is in [-1,1]
        if value_of_w > 1 or value_of_w < -1:
            raise Exception("Inertia coefficient has to be in [-1,1]")

        # cognitive coefficient is float in [0,3]
        if value_of_c1 < 0 or value_of_c1 > 3:
            raise Exception("Cognitive coefficient has to be in [0,3]")

        # social coefficient is float in [0,3]
        if value_of_c2 < 0 or value_of_c2 > 3:
            raise Exception("Social coefficient has to be in [0,3]")

        # the sum of cognitive and social coefficient is in [0.1,4.4]
        #c1_c2 = [value_of_c1, value_of_c2]
        #sum_of_c1_c2 = sum(c1_c2)
        #if sum_of_c1_c2 > 4.4 or sum_of_c1_c2 < 0.1:
            #raise Exception("The sum of cognitive and social coefficient has to be in [0.1,4.4]")

        #if flag:
        execute_pso()

    except Exception as e:
        message = message + str(e)
        print(message)

    return message


def execute_pso():
    # create particle vector based on number of particles
    search_in_pso = PSO(num_of_particles)
    particles_vector = [Particle() for _ in range(search_in_pso.num_of_particles)]
    search_in_pso.particles = particles_vector
    output = []

    i = 0
    # set local and global best position
    # for each iteration, update velocity and position
    while i < num_of_iterations:
        search_in_pso.set_pbest()
        search_in_pso.set_gbest()

        search_in_pso.search_iteration()
        i += 1

    print(num_of_iterations, num_of_particles, value_of_c2, value_of_c1, value_of_w, search_in_pso.gbest_position[0],
          search_in_pso.gbest_position[1], search_in_pso.gbest_value)

    output.append(num_of_iterations)
    output.append(num_of_particles)
    output.append(value_of_c2)
    output.append(value_of_c1)
    output.append(value_of_w)
    output.append(search_in_pso.gbest_position[0])
    output.append(search_in_pso.gbest_position[1])
    output.append(search_in_pso.gbest_value)

    # control on unit tests
    #if flag:
    read_to_csv(output)

    return output


# generate csv file for program output
def read_to_csv(output):
    # append result each time program is ran
    with open('pso_output.csv', 'a', newline='') as csvFile:

        csvwriter = csv.writer(csvFile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(output)

        csvFile.close()


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
    def __init__(self, number_of_particles):
        self.num_of_particles = number_of_particles
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

    args = parse_arguments(sys.argv[1:])
    num_of_iterations = args.num_iteration
    num_of_particles = args.num_particle
    value_of_w = args.w
    value_of_c1 = args.c1
    value_of_c2 = args.c2

    # flag is used for unit tests
    #execute = True
    #check_parameters_execute_pso(execute)
    check_parameters_execute_pso()




