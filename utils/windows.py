from subprocess import call

class Windows:
  def __init__(self):
    self.default_registry_file = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    self.registry_file = "C:\\Windows\\System32\\drivers\\etc\\hosts"
  
  def optimize(self):
    self.clear()
    self.update()
  
  def clear(self):
    self.registry_file = self.default_registry_file
    self.file = open(self.registry_file, "w")
    self.file.write("")
    self.file.close()
  
  def update(self):
    self.registry_file = self.default_registry_file
    self.file = open(self.registry_file, "w")
    self.file.write("")
    self.file.close()
