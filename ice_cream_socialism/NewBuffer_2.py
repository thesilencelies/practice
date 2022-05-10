#Now I'm gonna try and rewrite this idea but in the 'circular' overwrite style. I'll save the + 1 % stuff for the review later

class Ring_Buffer:
	def __init__(self, limit):
		self.limit = limit
		#self.head = 0
		#self.tail = 0
		self.count = 0
		#self.size = len(self.buf)
		self.buf = []
		
	def item_check(self, value):
		return self.buf[value]
			
	def printList(self, *kwargs):
		print(self.buf)
			
	def push(self, value):
		if self.count < self.limit:
			self.buf[self.count] = value #Okay, perfect, this has the same list assignment index out of range problem come up, perfect to discuss tonight :) 
			self.count += 1
		else:
			self.count = 0
			self.buf[self.count] = value
			self.count += 1
			
	def remove(self, *kwargs):
		if len(self.buf) >= 1:
			self.buf.pop(0)
			self.count -=1
		else:
			return None
			
key = Ring_Buffer(5)

key.push(1)

key.printList()
			
