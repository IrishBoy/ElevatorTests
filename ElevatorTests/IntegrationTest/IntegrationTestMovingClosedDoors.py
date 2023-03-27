from IntegrationTest import IntegrationTest


class IntegrationTestMovingClosedDoors(IntegrationTest):
     def __init__(self, author, info, elevator, start_service, end_service, 
                  smth_between_doors, selected_floor, output_action):
          super().__init__(author, info, elevator, start_service, end_service)
          self.smth_between_doors = smth_between_doors
          # Whicj floor was selected
          self.selected_floor = selected_floor
          # Which action should be done
          self.output_action = output_action

     def run(self):
          doors = self.doors()
          moving = self.startMove(doors)
          assert_result =  self.assertEqual(moving, self.output_action)
          return {
             "result": assert_result,
             "message": "" if assert_result == True else '''Integration test of 
                                                            1. Nothing between doors
                                                            2. Moving 
                                                            failed'''
          }


     def startMove(self, between_doors):
          moving = self.elevator.ElevatorMoving(between_doors, self.selected_floor)
          return moving

     def doors(self):
          doors_result = self.elevator.Doors(self.smth_between_doors)
          return doors_result