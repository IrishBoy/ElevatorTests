from UnitTest import UnitTest

class UnitTestMechProblem(UnitTest):
     def __init__(self, author, info, service_name, input_weight, output_call):
          super().__init__(author, info, service_name)
          self.input_weight = input_weight
          self.output_call = output_call

     def run():
          pass