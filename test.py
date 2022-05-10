class RingBuffer:
  """" TODO(stephen) docstring"""
  def __init__(self, ring_len, **kwargs):
   # super.__init__(**kwargs)
    self.ring_len = ring_len
    self.buf = []

  def push(self, value, overwrite=True):
    """ add value to the head of the buffer
        @par overwrite - whether or not to replace the tail if the buffer is full
     """
    pass

  def pop(self):
    """ remove an item from the tail """
    pass

  def __repr__(self) -> str:
    """ string represenation """
    return str(self.buf)

  def __getitem__(self, index):
    """ index relative to the head
      0 is head, -1 the oldest item, 1 the second newest
     """
    pass

if __name__ == "__main__":

  testlen = 10
  buffer = RingBuffer(testlen)


  for i in range(30):
    buffer.push(i)
    print(buffer)

  assert(buffer[1] == 28)
  buffer.push(5, overwrite=False)
  assert(buffer[0] != 5)
  buffer.pop()
  buffer.push(6)
  assert(buffer[0] == 6)
