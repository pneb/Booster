import multiprocessing

class Utils:
  def __init__(self):
    self.data = None
    self.process = None
  
  def execute(self, command, data=None):
    self.data = data
    self.process = multiprocessing.Process(target=self.command)
    self.process.start()
  
  def command(self):
    self.command(self.data)
