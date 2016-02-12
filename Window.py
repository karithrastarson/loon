import Tkinter
from World import World 
import time

CANVAS_SIZE = 500
WINDOW_WIDTH = 750
COVERAGE_RADIUS = 8
class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):

		
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()



	def initialize(self):
		#Variables and triggers
		self.runTrigger = 0
		self.world = World()
		
		self.grid()

		#Buttons
		button = Tkinter.Button(self, text=u"Step", command=self.stepClick)
		button.grid(column=0, row=0, sticky = 'NW')

		button = Tkinter.Button(self, text=u"Auto", command=self.autoClick)
		button.grid(column=0, row=1, sticky = 'NW')

		button = Tkinter.Button(self, text=u"Stop", command=self.stopClick)
		button.grid(column=0, row=2, sticky = 'NW')

		button = Tkinter.Button(self, text=u"Reset", command=self.resetClick)
		button.grid(column=0, row=3, sticky = 'NW')


		#Label - Title
		label = Tkinter.Label(self, anchor="nw", fg="black",bg="white",text="Output")
		label.grid(column=2, row=2)
		#Label - Output
		self.labelVariable = Tkinter.StringVar()
		
		label = Tkinter.Label(self,height="10", width = "30", textvariable=self.labelVariable,
			anchor="nw", fg="green",bg="black") 
		label.grid(column=2,row=3,sticky='N')

		#Canvas
		self.canvas = Tkinter.Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE)
		self.canvas.grid(column=1,row=3, sticky='N')
		#self.refreshCanvas()


	def stepClick(self):
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
			self.update()

		


	def stopClick(self):
		self.runTrigger = 0

	def resetClick(self):
		self.runTrigger = 0
		self.initialize()
	
	def output(self, str):
		s = '\n'
		s += str
		s += self.labelVariable.get()
		self.labelVariable.set(s)


			


'''
++++++++++++++++++++++++++++
++++++  	MAIN      ++++++
++++++++++++++++++++++++++++
'''

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('Simulation')
	app.mainloop()


