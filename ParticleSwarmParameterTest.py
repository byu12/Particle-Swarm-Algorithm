import unittest
import ParticleSwarm as psClass


class ParticleSwarmTest(unittest.TestCase):

    def test_arg_parse(self):

        result = psClass.parse_arguments(['100', '100', '0.3', '0.2', '0.5'])
        self.assertEqual(result.num_iteration, 100)
        self.assertEqual(result.num_particle, 100)
        self.assertEqual(result.w, 0.3)
        self.assertEqual(result.c1, 0.2)
        self.assertEqual(result.c2, 0.5)

    def test_invalid_num_of_particles(self):

        psClass.num_of_iterations = 100
        psClass.num_of_particles = -10
        return_message = psClass.check_parameters_execute_pso(False)
        self.assertTrue('Invalid'.lower() in return_message.lower())

    def test_invalid_num_of_iterations(self):

        psClass.num_of_iterations = -1
        psClass.num_of_particles = 10
        return_message = psClass.check_parameters_execute_pso(False)
        self.assertTrue('Invalid'.lower() in return_message.lower())

    def test_invalid_value_of_w_positive(self):

        psClass.num_of_iterations = 10
        psClass.num_of_particles = 10
        psClass.value_of_w = 2
        return_message = psClass.check_parameters_execute_pso(False)
        self.assertTrue('Invalid'.lower() in return_message.lower())

    def test_invalid_value_of_w_negative(self):

        psClass.num_of_iterations = 10
        psClass.num_of_particles = 10
        psClass.value_of_w = -2
        return_message = psClass.check_parameters_execute_pso(False)
        self.assertTrue('Invalid'.lower() in return_message.lower())

    def test_invalid_value_of_c1c2(self):
        psClass.num_of_iterations = 10
        psClass.num_of_particles = 10
        psClass.value_of_w = 0.3
        psClass.value_of_c1 = 10
        psClass.value_of_c2 = 0.5
        return_message = psClass.check_parameters_execute_pso(False)
        self.assertTrue('Invalid'.lower() in return_message.lower())


if __name__ == '__main__':
    unittest.main()

