from .. import Test

class IntegrationTest(Test):
     def __init__(self, author, info, start_service, end_service):
          super().__init__(author, info)
          self.service_name = start_service
          self.end_service = end_service