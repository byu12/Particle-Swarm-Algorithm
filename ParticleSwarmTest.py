import unittest
import ParticleSwarm as psClass


class ParticleSwarmTest(unittest.TestCase):

    def test_ackley_positive(self):

        print("start of test_ackley_positive.\n")
        num_of_particles = 50
        target_error = 0.01
        result_arr = []
        search_in_pso = psClass.PSO(0, target_error, num_of_particles)
        particles_vector = [psClass.Particle() for _ in range(search_in_pso.num_of_particles)]
        search_in_pso.particles = particles_vector

        for p in search_in_pso.particles:
            result = search_in_pso.ackley(p.position)
            result_arr.append(result)

        self.assertGreater(min(result_arr), 0)
        print("Ackley function is positive.")
        print("end of test_ackley_positive.\n")

    def test_ackley_minimum(self):

        print("start of test_ackley_minimum.\n")
        result = psClass.PSO.ackley(psClass.PSO, [0, 0])

        self.assertEqual(result, float(0))
        print("In Ackley function is f(0,0)=0")
        print("end of test_ackley_minimum.\n")

    def test_pso_parameterOptionOne(self):

        print("start of test_pso_parameterOptionOne.\n")
        psClass.target_error = 0.01
        psClass.num_of_particles = 100
        psClass.num_of_iterations = 100
        psClass.value_of_w = 0.1
        psClass.value_of_c1 = 0.2
        psClass.value_of_c2 = 0.3

        arr = psClass.execute_pso()

        self.assertGreater(0.1, abs(arr[5]))
        self.assertGreater(0.1, abs(arr[6]))

        print("end of test_pso_parameterOptionOne.\n")

    def test_pso_parameterOptionTwo(self):

        print("start of test_pso_parameterOptionTwo.\n")
        psClass.target_error = 0.0001
        psClass.num_of_particles = 100
        psClass.num_of_iterations = 100
        psClass.value_of_w = 0.3
        psClass.value_of_c1 = 0.2
        psClass.value_of_c2 = 0.5

        arr = psClass.execute_pso()

        self.assertGreater(0.1, abs(arr[5]))
        self.assertGreater(0.1, abs(arr[6]))

        print("end of test_pso_parameterOptionTwo.\n")

    def test_pso_parameterOptionThree(self):

        print("start of test_pso_parameterOptionThree.\n")
        psClass.target_error = 0.0001
        psClass.num_of_particles = 50
        psClass.num_of_iterations = 50
        psClass.value_of_w = 0.3
        psClass.value_of_c1 = 0.2
        psClass.value_of_c2 = 0.5

        arr = psClass.execute_pso()

        self.assertGreater(0.1, abs(arr[5]))
        self.assertGreater(0.1, abs(arr[6]))

        print("end of test_pso_parameterOptionThree.\n")


if __name__ == '__main__':
    unittest.main()

