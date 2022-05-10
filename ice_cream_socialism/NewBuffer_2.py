class RingBuffer:

    def __init__(self, limit):

        self.limit = limit

        # self.head = 0

        # self.tail = 0
        self.index = 0

        # self.size = len(self.buf)

        self.buf = []

    def item_check(self, value):
        return self.buf[(self.index % self.limit) - value - 1]

    def get_head(self):
        """ returns the newest value from the buffer"""
        # return self.buf[self.index - 1]
        return self.item_check(0)

    def printList(self, **kwargs):
        print(self.buf)

    def push(self, value, overwrite=True):
        if len(self.buf) < self.limit:
            self.buf.insert(self.index, value)
            self.index += 1
        else:
            if overwrite:
                if self.index >= self.limit:
                    self.index = 0
                self.buf[self.index] = value
                self.index += 1

    def pop(self):
        if len(self.buf) >= 1:
            rval = self.buf.pop(self.index % self.limit)
            self.index -= 1
            return rval
        else:
            return None

    def __repr__(self) -> str:
        """ string represenation """
        return str(self.buf)

    def __getitem__(self, index):
        """ index relative to the head  0 is head, -1 the oldest item, 1 the second newest
          """
        return self.item_check(index)


if __name__ == "__main__":
    def testfun(testlen):
        buffer = RingBuffer(testlen)
        for i in range(30):
            buffer.push(i)
            print(buffer)
        print(buffer.get_head())
        assert(buffer.get_head() == 29)

        assert(buffer[1] == 28)
        buffer.push(500, overwrite=False)  # should fail
        assert(buffer[0] != 500)
        assert(buffer.pop() == 30 - testlen)
        print(buffer[0])
        buffer.push(6)
        print(buffer)
        print(buffer[0])
        assert(buffer[0] == 6)

    for i in range(5, 20, 3):
        testfun(i)
