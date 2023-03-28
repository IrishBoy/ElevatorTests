from ValidationTest import VailidationTest

class ValidationTestUseCase1(VailidationTest):
     def __init__(self, author, info, elevator, services_list, input_parametrs, output_parameters):
          super().__init__(author, info, elevator, services_list, input_parametrs, output_parameters)

     
     def run(self):
          doors = self.doors()
          moving = self.startMove(doors)
          floorStop = self.stop(moving)
          openDoor = self.openDoor(floorStop)
          assert_result =  self.assertEqual([doors, moving, floorStop, openDoor], self.output_parameters)
          return {
             "result": assert_result,
             "message": "" if assert_result == True else '''Validation test based on use case 1 failed'''
          }


     def openDoor(self, floorStop):
          opedDoorPar = self.elevator.DoorOpened(floorStop, self.input_parametrs["DoorOpened"])
          return opedDoorPar

     def stop(self, moving):
          stop = self.elevator.StopAtFloof(moving, self.input_parametrs["right_floor"])
          return stop
     
     def startMove(self, between_doors):
          moving = self.elevator.ElevatorMoving(between_doors,self.input_parametrs["selected_floor"])
          return moving

     def doors(self):
          doors_result = self.elevator.Doors(self.input_parametrs["smth_between_doors"])
          return doors_result