from UnitTest import UnitTest
import unittest


class UnitTestMechProblem(UnitTest):
    def __init__(self, author, info, service_name, input_problem, output_call):
        super().__init__(author, info, service_name)
        # Problem that occures
        self.input_problem = input_problem
        # Emergency call that should be raised
        self.output_call = output_call

    def run(self):
        assert_result = self.assertEqual(self.elevator.Stuck(self.input_problem), self.output_call)
        return {
             "result": assert_result,
             "message": "" if assert_result == True else "Stuck Mech does not work properly"
        }