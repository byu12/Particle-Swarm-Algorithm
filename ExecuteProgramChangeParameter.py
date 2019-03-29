import subprocess

path = "C:\\Users\\yubo\\PycharmProjects\\Particle-Swarm-Algorithm\\dist\\ParticleSwarm\\ParticleSwarm.exe"


# function to get n decimal space of a decimal number
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def change_num_iterations():
    num_of_particles = "50"
    value_of_w = "0"
    value_of_c1 = "1.5"
    value_of_c2 = "1.5"
    i = 0
    n = 1
    while n < 101:
        num_of_iterations = n
        print("number of iterations is: %d" % num_of_iterations)
        subprocess.check_call([path, str(num_of_iterations), num_of_particles, value_of_w, value_of_c1, value_of_c2])
        i += 1
        n = i*5


def change_num_particles():
    num_of_iterations = "50"
    value_of_w = "0"
    value_of_c1 = "1.5"
    value_of_c2 = "1.5"
    i = 0
    n = 1
    while n < 101:
        num_of_particles = n
        print("number of particles is: %d" % num_of_particles)
        subprocess.check_call([path, num_of_iterations, str(num_of_particles), value_of_w, value_of_c1, value_of_c2])
        i += 1
        n = i*5


# w is in [-1,1]
def change_inertia_weight():
    num_of_particles = "50"
    num_of_iterations = "50"
    value_of_c1 = "1.5"
    value_of_c2 = "1.5"
    n = -1.0
    while n <= 1.0:
        value_of_w = truncate(n, 1)
        print("inertia weight is: %f" % value_of_w)
        subprocess.check_call([path, num_of_iterations, num_of_particles, str(value_of_w), value_of_c1, value_of_c2])
        n = n + 0.1


# c1 is in [0,3]
def change_c1():
    num_of_particles = "50"
    num_of_iterations = "50"
    value_of_w = "0"
    value_of_c2 = "1.5"
    n = 0.1
    while n < 3.0:
        value_of_c1 = truncate(n, 4)
        print("cognitive coefficient is: %f" % value_of_c1)
        subprocess.check_call([path, num_of_iterations, num_of_particles, value_of_w, str(value_of_c1), value_of_c2])
        n = n + 0.14


# c2 is in [0,3]
def change_c2():
    num_of_particles = "50"
    num_of_iterations = "50"
    value_of_w = "0"
    value_of_c1 = "1.5"
    n = 0.1
    while n < 3.0:
        value_of_c2 = truncate(n, 4)
        print("inertia weight is: %f" % value_of_c2)
        subprocess.check_call([path, num_of_iterations, num_of_particles, value_of_w, value_of_c1, str(value_of_c2)])
        n = n + 0.14


# main function to execute functions
if __name__ == "__main__":
    # add rounding error for all
    for x in range(5):
        change_num_iterations()
        change_num_particles()
        change_inertia_weight()  # break at 0
        change_c1()
        change_c2()



