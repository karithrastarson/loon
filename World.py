'''
Created by: Kari Thrastarson,2016

This is the WORLD in which the model is run.

The file contains the data structures and all the 
data created during the run.

Helper classes are Balloon.py and Current.py
'''

from Balloon import Balloon
from Current import Current
class World:

	def __init__(self):
		self.GRID_SIZE = 10
		self.grid = [[0 for x in range(self.GRID_SIZE)] for x in range(self.GRID_SIZE)] 

		self.allBalloons = [];

		for x in range(10):
			self.allBalloons.append(Balloon());




	def applyCurrents(self):
		for b in self.allBalloons:
			self.grid[b.getX()][b.getY()] = 0
			b.applyCurrent()
			self.grid[b.getX()][b.getY()] = 1

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





