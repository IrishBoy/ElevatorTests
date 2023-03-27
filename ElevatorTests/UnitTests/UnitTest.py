from .. import Test


class UnitTest(Test):
     def __init__(self, author, info, service_name, elevator):
        super().__init__(author, info, elevator)
        # Which service is tested
        self.service_name = service_name