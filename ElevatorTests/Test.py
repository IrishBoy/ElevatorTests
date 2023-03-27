import datetime
import json

class Test():
     def __init__(self, author, info, elevator):
          self.date = datetime.datetime.now()
          self.author = author
          self.info = info
          self.result = None
          self.elevator = elevator