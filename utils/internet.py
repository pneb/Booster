from utils.utils import Utils
from utils.sockets import Sockets

class Internet:
  def __init__(self):
    self.utils = Utils()
    self.sockets = Sockets()
  
  def boost(self):
    self.utils.execute(self.command)
  
  def command(self):
    self.sockets.open()
    self.sockets.close()
