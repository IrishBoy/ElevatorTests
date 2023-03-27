from .. import Test

class VailidationTest(Test):
     def __init__(self, author, info, elevator, services_list, input_parametrs, output_parameters):
          super().__init__(author, info, elevator)
          self.services_list = services_list
          self.input_parametrs = input_parametrs
          self.output_parameters = output_parameters