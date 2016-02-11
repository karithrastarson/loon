import Tkinter
from World import World 
import time

CANVAS_SIZE = 500
COVERAGE_RADIUS = 8
class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		
		self.world = World()
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		
		self.initialize()



	def initialize(self):
		#Variables and triggers
		self.runTrigger = 0
		
		
		self.grid()

		#Buttons
		button = Tkinter.Button(self, text=u"Step", command=self.stepClick)
		button.grid(column=0, row=0)

		button = Tkinter.Button(self, text=u"Auto", command=self.autoClick)
		button.grid(column=0, row=1)

		button = Tkinter.Button(self, text=u"Stop", command=self.stopClick)
		button.grid(column=0, row=2)

		button = Tkinter.Button(self, text=u"Reset", command=self.resetClick)
		button.grid(column=0, row=3,sticky='N')

		#Label
		#label = Tkinter.Label(self, anchor="w", fg="white",bg="blue") 
		#label.grid(column=0,row=1,columnspan=2,sticky='EW')

		#Canvas
		self.canvas = Tkinter.Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE)

		self.canvas.grid(column=1,row=3)
		#self.refreshCanvas()


	def stepClick(self):
		print("You clicked STEP button !")
		self.world.applyCurrents()
		self.world.moveDecisions()
		self.canvas.delete("all")
		for b in self.world.allBalloons:
			self.canvas.create_oval(b.getX()-COVERAGE_RADIUS,b.getY()-COVERAGE_RADIUS,b.getX()+COVERAGE_RADIUS,b.getY()+COVERAGE_RADIUS, fill="blue")
			self.canvas.create_oval(b.getX()-4,b.getY()-4,b.getX()+4,b.getY()+4, fill="red")
			self.canvas.create_line(b.getX(),b.getY(), b.getX()+b.getCurrent().getX(), b.getY()+b.getCurrent().getY(),arrow="last")
			


	def autoClick(self):
		self.runTrigger = 1
		while(self.runTrigger):
			self.stepClick()
			time.sleep(1)

	def stopClick(self):
		print("You clicked STOP button !")
		self.runTrigger = 0

	def resetClick(self):
		print("You clicked RESET button !")

			


'''
++++++++++++++++++++++++++++
++++++  	MAIN      ++++++
++++++++++++++++++++++++++++
'''

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('Simulation')
	app.mainloop()


