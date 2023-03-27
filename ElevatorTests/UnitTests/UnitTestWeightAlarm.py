from UnitTest import UnitTest
import unittest


class UnitTestWeightAlarm(UnitTest):
    def __init__(self, author, info, service_name, elevator, input_weight, output_alarm):
        super().__init__(author, info, service_name, elevator)
        self.input_weight = input_weight
        self.output_alarm = output_alarm

    def run(self):
        assert_result = self.assertEqual(self.elevator.WeightAlarm(self.input_weight), self.output_alarm)
        return {
             "result": assert_result,
             "message": "" if assert_result == True else "Weight Alarm does not work properly"
        }
