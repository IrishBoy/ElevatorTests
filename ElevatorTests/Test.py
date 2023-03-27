import datetime
import json

class Test():
     def __init__(self, author, info, elevator):
          self.date = datetime.datetime.now()
          # Who runs this test
          self.author = author
          # General info about test
          self.info = info
          # placeholder
          self.result = None
          # Non existing elevator module
          self.elevator = elevator