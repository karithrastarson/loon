'''
Created by: Kari Thrastarson,2016

This is the WORLD in which the model is run.

The file contains the data structures and all the 
data created during the run.

Helper classes are Balloon.py and Current.py
'''
import random
import csv
from Balloon import Balloon
from Current import Current


class World:

#Constructor
	def __init__(self):
		#The size of the grid for the balloons
	

		self.GRID_SIZE = 200
		self.WINDOW_WIDTH = self.GRID_SIZE + 250
		self.COVERAGE_RADIUS = 8
		self.grid = [[[] for x in range(self.GRID_SIZE)] for x in range(self.GRID_SIZE)] 
		self.coverage = 0
		self.noBalloons = 0
		#Overlap is the number of balloons that exceed each balloon in a cell. So if 3 balloons occupy one cell, that cell gives 2 overlaps
		self.overlaps = 0

#Read weatherdata
		self.stratosphere = []
		with open('weatherdata.txt', 'r') as f:
			reader = csv.reader(f, dialect='excel', delimiter='\t')
			for row in reader:
				newCurrent =  Current(int(row[0]),int(row[1]),int(row[2]))
				self.stratosphere.append(newCurrent)

		self.allBalloons = [];
#Add the balloons to the grid
		for i in range(self.GRID_SIZE):
			self.generateBalloon()
			
			
			


	def applyCurrents(self):
		for b in self.allBalloons:
			curX = b.getX()
			curY = b.getY()
			curNoB = len(self.grid[curX][curY])
			if curNoB > 1:
				self.overlaps-=1

			self.grid[curX][curY].remove(b)	
			#self.removeBalloon(b)
			b.applyCurrent()
			self.adjustPosition(b)
			self.grid[b.getX()][b.getY()].append(b)
			if len(self.grid[b.getX()][b.getY()]) > 1:
				self.overlaps += 1


	def moveDecisions(self):
		for b in self.allBalloons:
			x = b.getX()
			y = b.getY()
			w = b.getCurrentLayer()

			if len(self.grid[x][y]) > 1:
				#Multiple balloons same spot. Need to change
				if w == 0:
					newCurrent = 1
				elif w==(len(self.stratosphere)-1):
					newCurrent = w-1
				else:
					newCurrent = random.randint(-1,1)
					newCurrent = w+newCurrent

				
				b.changeCurrent(self.stratosphere[newCurrent], newCurrent)

	def adjustPosition(self,b):
		if b.getX() >= self.GRID_SIZE:
			b.setX(b.getX()-self.GRID_SIZE)
		if b.getY() >= self.GRID_SIZE:
			b.setY(b.getY()-self.GRID_SIZE)
		if b.getX() < 0:
			b.setX(self.GRID_SIZE+b.getX())
		if b.getY() < 0:
			b.setY(self.GRID_SIZE+b.getY())
		

	def returnStats(self):
		t = "Number of balloons: " + str(self.noBalloons)
		t += "\n Number of overlaps: " + str(self.overlaps)
		t += "\n Current coverege: " + str(100*(self.noBalloons-self.overlaps)/(self.GRID_SIZE*self.GRID_SIZE)) + "%"

		return t

	def generateBalloon(self, x=0, y=0):
		#Function that generates a new balloon and makes sure all statistcs are updated accordingly
		cur = 0
		#The balloon is deployed into the lowest current
		newBalloon = Balloon(x,y,cur,self.stratosphere[cur])

		#Added to the list of balloons
		self.allBalloons.append(newBalloon)

		#Book keeping
		self.noBalloons += 1

		#Added to the grid of balloons
		self.grid[x][y].append(newBalloon)

		#If this grid position has a balloon, then overlap++
		if len(self.grid[x][y]) > 1:
			self.overlaps += 1








