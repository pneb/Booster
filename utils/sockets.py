from socket import socket

class Sockets:
  def __init__(self):
    self.socket = socket()
    self.host = "google.com"
    self.port = 80
  
  def open(self, cmd=None):
    self.socket = socket()
    self.socket.connect((self.host, self.port))
    self.socket.send(b"GET / HTTP/1.0\n\n")
  
  def close(self, cmd=None):
    self.socket.close()
