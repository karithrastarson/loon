
import random
from Balloon import Balloon
from Current import Current
import random
from tkinter import *

#Variables and lists used in the simulation
#Size of the grid for the balloons
GRID_SIZE = 500
#Stratosphere is the list of currents
stratosphere = [Current(1,3), Current(-3, -3), Current(7,3)]
#Grid is an overview of the positions of the balloons
grid = [[0 for x in range(GRID_SIZE)] for x in range(GRID_SIZE)] 
#List of balloons in the simulations
allBalloons = [];
#END OF VARIABLES

#Populate the allBalloons list
for x in range(GRID_SIZE):
	cur = random.randint(0,2)
	allBalloons.append(Balloon(0,0,stratosphere[cur]));
	grid[0][0] += 1

#c = Canvas()
c = Canvas(width=GRID_SIZE, height=GRID_SIZE)
c.pack()

#circle = c.create_oval(100,100,110,110, fill="red")

def applyCurrents():
		for b in allBalloons:
			grid[b.getX()][b.getY()] -= 1
			b.applyCurrent()
			grid[b.getX()][b.getY()] += 1
def adjustPosition(b):
	if b.getX() >= GRID_SIZE:
		b.setX((b.getX()-GRID_SIZE))
	if b.getY() >= GRID_SIZE:
		b.setY((b.getY()-GRID_SIZE))


def simulate():
    #one step of simulation
    #Run decision algorithm
    #runDecisions()

    #Move all balloons to their new position

    #Then delete all objects
    c.delete("all")
    #Then draw all balloons on their new position
    for b in allBalloons:
        b.applyCurrent()
        adjustPosition(b)
        circle = c.create_oval(b.getX()-5,b.getY()-5,b.getX()+5,b.getY()+5, fill="red")
        c.pack()
    
    c.after(100, simulate)


c.after(100, simulate)
c.mainloop()