from utils.utils import Utils
from utils.windows import Windows

class Booster:
  def __init__(self):
    self.utils = Utils()
    self.windows = Windows()
  
  def boost(self):
    self.utils.execute(self.command)
  
  def command(self):
    self.windows.optimize()
