from dataclasses import dataclass
import re


class RingBuffer:
  """" TODO(stephen) docstring"""
  def __init__(self, ring_len=8, **kwargs):
   # super.__init__(**kwargs)
    self.ring_len = ring_len
    self.buf = []
    self.front= 0
    self.rear = 0
    self.size = 0


  def at_limit(self):
    return self.ring_len == self.size


  def push(self, value, overwrite=True):
    if (self.at_limit()):
      raise Exception("Ring at Limit!!!")
    self.buf[self.rear] = value
    self.rear = (self.rear + 1) % self.ring_len #internet told me this part
    self.size +=1 

  def pop(self):
    if(self.size == 0):
      return None
    value = self.buf[self.front]
    self.front = (self.front + 1) % self.ring_len #likewise
    self.size -= 1
    return value
    
  def showBuffer(self) -> str:
    return str(self.buf)

  def __getitem__(self, index):
    """ index relative to the head
      0 is head, -1 the oldest item, 1 the second newest
     """
    return self.buf[index]

if __name__ == "__main__":

  testlen = 10
  buffer = RingBuffer(testlen)


  buffer.push(2)


 

  # assert(buffer[1] == 28)
  # buffer.push(5, overwrite=False)
  # assert(buffer[0] != 5)
  # buffer.pop()
  # buffer.push(6)
  # assert(buffer[0] == 6) 