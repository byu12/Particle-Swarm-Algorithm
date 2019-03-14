import unittest

import ParticleSwarmParameterTest
import ParticleSwarmTest

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(ParticleSwarmParameterTest))
suite.addTests(loader.loadTestsFromModule(ParticleSwarmTest))

# initialize a runner and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
