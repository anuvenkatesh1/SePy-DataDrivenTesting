'''
Created on Sep 18, 2017

@author: labinav
'''
import unittest
 
from scenarios.scenario_a import TestScenarioA
 
 
# load test cases
scenario_a = unittest.TestLoader().loadTestsFromTestCase(TestScenarioA)
 
# create test suite
test_suite = unittest.TestSuite([scenario_a])
 
# execute test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)