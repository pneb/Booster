class Handler:
  def __init__(self, internet, booster):
    self.internet = internet
    self.booster = booster
  
  def boost(self):
    self.internet.boost()
    self.booster.boost()
