'''
Created by: Kári Þrastarson,2016

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
		self.GRID_SIZE = 10
		self.grid = [[0 for x in range(self.GRID_SIZE)] for x in range(self.GRID_SIZE)] 

#To begin with the available currents are the 3
		self.stratosphere = [Current(1,3), Current(-3, 3), Current(0,3)]

		self.allBalloons = [];
#Add the balloons to the grid
		for x in range(self.GRID_SIZE):
			cur = random.randint(0,2)
			self.allBalloons.append(Balloon(0,0,self.stratosphere[cur]));
			self.grid[0][0] += 1




	def applyCurrents(self):
		for b in self.allBalloons:
			self.grid[b.getX()][b.getY()] -= 1
			b.applyCurrent()
			self.grid[b.getX()][b.getY()] += 1

	def printGrid(self):
		for i in range(self.GRID_SIZE):
			print(" ")
			for j in range(self.GRID_SIZE):
				print (self.grid[i][j], end="")


w = World()

w.applyCurrents()
w.printGrid()
wait = input("PRESS ENTER TO CONTINUE.")
w.applyCurrents()
w.printGrid()
wait = input("PRESS ENTER TO CONTINUE.")
w.applyCurrents()
w.printGrid()





