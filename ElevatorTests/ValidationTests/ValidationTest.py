from .. import Test

class VailidationTest(Test):
     def __init__(self, author, info, service_names):
          super().__init__(author, info)
          self.service_names = service_names
          # self.end_service = end_service