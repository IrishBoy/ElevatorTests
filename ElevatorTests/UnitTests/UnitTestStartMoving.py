from UnitTest import UnitTest
import unittest


class UnitTestStartMoving(UnitTest):
    def __init__(self, author, info, service_name, selected_floor, output_action):
        super().__init__(author, info, service_name)
        # Whicj floor was selected
        self.selected_floor = selected_floor
        # Which action should be done
        self.output_action = output_action

    def run(self):
        assert_result = self.assertEqual(self.elevator.ElevatorMoving(self.selected_floor), self.output_action)
        return {
             "result": assert_result,
             "message": "" if assert_result == True else "Elevator Moving does not work properly"
        }