import random
import numpy
import math

twopi = 2 * math.pi


class Particle:
    # initialize properties of particle including current position,
    # global best, local best and velocity
    def __init__(self):
        # default constructor
        # initialize random positive and negative numbers of x and y in range (-15,15)
        self.position = numpy.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 15,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 15])
        self.pbest_p = self.position
        self.pbest_v = float('inf')
        self.velocity = numpy.array([0, 0])

    def __str__(self):
        print("The position of the particle is %s, the local best position is %s" % (self.position, self.pbest_p))

    # the next position of the particle is current position + its velocity
    def update_postition(self):
        self.position = self.position + self.velocity


class PSO:
    # parameterized constructor
    def __init__(self, target, num_of_particles):
        self.target = target
        self.num_of_particles = num_of_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = numpy.array([random.random() * 15, random.random() * 15])

    # The formula of Ackley function from wikipedia
    # this is Ackley function in its 2 dimensional domain
    def ackley(self, particle):
        x = particle.position[0]
        y = particle.position[1]
        p1 = (-20) * math.exp((-0.2) * math.sqrt(0.5*((x*x)+(y*y))))
        p2 = math.exp(0.5*(math.cos(twopi * x)+ math.cos(twopi * y)))
        result = p1 - p2 + math.e + 20
        return result

    # set the local best value
    # the function value less than local best
    # update function value as local best
    def set_pbest(self):
        for particle in self.particles:
            fitness_value = self.ackley(particle)
            if particle.pbest_v > fitness_value:
                particle.pbest_v = fitness_value
                particle.pbest_p = particle.position

    # set the global best value
    # if the function value is less than global best
    # update function value as global best
    def set_gbest(self):
        for particle in self.particles:
            best_fitness_value = self.ackley(particle)
            if self.gbest_value > best_fitness_value:
                self.gbest_value = best_fitness_value
                self.gbest_position = particle.position

    # search through all iterations
    # update velocity of the next particle
    # update the position of the next particle
    def search_iteration(self):
        for particle in self.particles:
            global value_of_w
            new_velocity = (value_of_w * particle.velocity) + (value_of_c1 * random.random()) * (
                        particle.pbest_p - particle.position) + \
                           (random.random() * value_of_c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.update_postition()

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()


# main function to execute iterations
if __name__ == "__main__":

    try:
        # user to enter number of iterations, particles, inertia weight w, acceleration coefficient c1 and c2
        num_of_iterations = int(input("What is the number of iterations? "))
        num_of_particles = int(input("What is the number of particles? "))
        value_of_w = float(input("What is the value of inertia weight? "))
        value_of_c1 = float(input("What is the value of personal acceleration coefficient? "))
        value_of_c2 = float(input("What is the value of social acceleration coefficient? "))

        search_in_pso = PSO(0, num_of_particles)
        particles_vector = [Particle() for _ in range(search_in_pso.num_of_particles)]
        search_in_pso.particles = particles_vector
        search_in_pso.print_particles()

        i = 0
        while i < num_of_iterations:
            search_in_pso.set_pbest()
            search_in_pso.set_gbest()
            search_in_pso.search_iteration()
            i += 1

        print("The global best solution is: %s, this is achieved at iteration %s" % (search_in_pso.gbest_position, i))

    except ValueError as e:
        print("Please provide a correct format of input! " + str(e))
