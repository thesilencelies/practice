# Okay, so this is the very first thing I had in mind way bck when you were first explaining the qeue vs stack system to me. I now understand how it's not what you were looking for, now I just gotta get the other version to work too :)'

# This one is like a one way conveyerbelt where it always adds the next item to the end of the array and pushes everything left (you know, cuts off the furthest left ends jawn)


# works but is inefficient - O(N) inserts

class RingBuffer:
    def __init__(self, limit):
        self.limit = limit
        self.buf = []

    def item_check(self, value):
        return self.buf[-1 - value]

    def printList(self, **kwargs):
        print(self.buf, kwargs)

    def push(self, value, overwrite=True):
        if len(self.buf) < self.limit:
            self.buf.append(value)
        else:
            if overwrite:
                self.buf = self.buf[slice(1, self.limit)]
                self.buf.append(value)

    def pop(self, **kwargs):
        if len(self.buf) >= 1:
            return self.buf.pop(0)
        else:
            return None

    def __repr__(self) -> str:
        """ string represenation """
        return str(self.buf)

    def __getitem__(self, index):
        """ index relative to the head
          0 is head, -1 the oldest item, 1 the second newest
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
        buffer.push(6)
        assert(buffer[0] == 6)

    for i in range(5, 20, 3):
        testfun(i)
