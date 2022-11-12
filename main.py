from utils.internet import Internet
from utils.booster import Booster
from utils.handler import Handler

internet = Internet()
booster = Booster()

if __name__ == "__main__":
  # Boost the internet connection
  handler = Handler(internet, booster)
  handler.boost()
