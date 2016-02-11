'''
Created by: Kari Thrastarson,2016

This is the WORLD in which the model is run.

The file contains the data structures and all the 
data created during the run.

Helper classes are Balloon.py and Current.py
'''
import random

from Balloon import Balloon
from Current import Current

class World:

#Constructor
	def __init__(self):
		#The size of the grid for the balloons
		self.GRID_SIZE = 500
		self.grid = [[[None] for x in range(self.GRID_SIZE)] for x in range(self.GRID_SIZE)] 

#To begin with the available currents are the 3
		self.stratosphere = [Current(10,35), Current(-53, 43), Current(20,33)]
		self.allBalloons = [];
#Add the balloons to the grid
		for x in range(self.GRID_SIZE):
			cur = random.randint(0,2)
			self.allBalloons.append(Balloon(0,0,self.stratosphere[cur]));
			self.grid[0][0].append(Balloon(0,0,self.stratosphere[cur]))


	def applyCurrents(self):
		for b in self.allBalloons:
			b.applyCurrent()
			self.adjustPosition(b)
			self.grid[b.getX()][b.getY()].append(b)

	def moveDecisions(self):
		for b in self.allBalloons:
			x = b.getX()
			y = b.getY()
			if len(self.grid[x][y]) > 1:
				newCurrent = random.randint(0,2)
				b.changeCurrent(self.stratosphere[newCurrent])

	def adjustPosition(self,b):
		if abs(b.getX()) >= self.GRID_SIZE:
			b.setX((abs(b.getX())-self.GRID_SIZE))
		if abs(b.getY()) >= self.GRID_SIZE:
			b.setY((abs(b.getY())-self.GRID_SIZE))
	#def simulate(self):
		#self.gui.simulate()


#w = World()
#w.simulate()







