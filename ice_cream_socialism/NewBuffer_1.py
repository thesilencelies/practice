#Okay, so this is the very first thing I had in mind way bck when you were first explaining the qeue vs stack system to me. I now understand how it's not what you were looking for, now I just gotta get the other version to work too :)'

class Ring_Buffer:
	def __init__(self, limit):
		self.limit = limit 
		self.count = 0
		#self.head = 0
		#self.tail = 0
		#self.size = 0
		self.buf = []
		
	def item_check(self, value):
		return self.buf[value]
			
	def printList(self, *kwargs):
		print(self.buf)
			
	def push(self, value):
		if self.count < self.limit:
			self.buf.append(value)
			self.count += 1
		else:
			self.buf = self.buf[slice(1, self.limit)]
			self.buf.append(value)
			
	def remove(self, *kwargs):
		if len(self.buf) >= 1:
			self.buf.pop(0)
			self.count -=1
		else:
			return None
			
		
key = Ring_Buffer(5)
	
for i in range(0,10):
	key.push(i)
	
key.printList()

key.remove()

key.printList()

key.push(10)

key.printList()

key.push(11)

key.printList()
	
#for i in range(0,5):
#	key.item_check(i)
