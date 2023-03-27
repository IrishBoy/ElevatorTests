from .. import Test

class IntegrationTest(Test):
     def __init__(self, author, info, elevator, start_service, end_service):
          super().__init__(author, info, elevator)
          self.service_name = start_service
          self.end_service = end_service