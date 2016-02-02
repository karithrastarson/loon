from Current import Current
class Balloon:

	#Constructor which gives starting position
	def __init__(self,startX=0, startY=0, c=Current(1,3)):
		self.x = startX
		self.y = startY
		self.wind = c

	#Get and set functions
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def setX(self, newX):
		self.x = newX
	def setY(self, newY):
		self.y = newY
	def getCurrent(self):
		return self.wind
	def applyCurrent(self):
		self.x = self.x + self.wind.getX()
		self.y = self.y + self.wind.getY()

