

class RingBuffer:
  pass



if __name__ == "__main__":

  testlen = 10
  buffer = RingBuffer(testlen)

  buffer.add(5, overwrite=False)
  buffer.