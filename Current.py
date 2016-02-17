class Current:
	
	#
	def __init__(self,i=0, xx=0, yy=0):
		self.id = i
		self.x = xx
		self.y = yy

	def __eq__(self, other):
		test1 = (self.getX() == other.getX())
		test2 = (self.getY() == other.getY())

		return (test1 and test2)

	def setX(self,xx):
		self.x = xx
	def setY(self,yy):
		self.y = yy
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getId(self):
		return self.id




