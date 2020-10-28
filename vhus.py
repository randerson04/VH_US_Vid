'''
Program: vhus.py
Author: Ryan 10/21/2020

Final GUI-based project for the python module for VH-US Old School Video Store that calculates the final cost of the your video rentals.
'''

from breezypythongui import EasyFrame
from tkinter.font import Font 

class VhusVideo(EasyFrame):
	'''displays a greeting in a window'''
	
	def __init__(self):
		'''sets up the window and the widgets'''
		EasyFrame.__init__(self, title = "VH-US Old School Videos", background = 'green')
		fontOne = Font(family = 'Georgia', size = 18)
		fontTwo = Font(family = 'Arial', size = 14)

		#add label widgets
		self.addLabel(text = 'VH-Us Old School Videos', row = 0, column = 0, columnspan = 2, background = 'green', font = fontOne)
		self.addLabel(text = 'Please Enter Number of Old Videos: ', row = 1, column = 0, background = 'green', font = fontTwo)
		self.addLabel(text = 'Please Enter Number of New Videos: ', row = 2, column = 0, background = 'green', font = fontTwo)
		self.addLabel(text = 'Total Cost of Videos', row = 4, column = 0, background = 'green', font = fontTwo)

		#adds entry fields
		self.oldVid = self.addIntegerField(value = 0, row = 1, column = 1)
		self.newVid = self.addIntegerField(value = 0, row = 2, column = 1)
		self.totalVid = self.addFloatField(value = 0.00, row = 4, column = 1, precision = 2, state = 'readonly')

		#add button command
		self.addButton(text = 'RENT', row = 3, column = 0, columnspan = 4, command = self.vidTot)

	#event handling method
	def vidTot(self):
		#vars for cost
		oldRental = 2.00
		newRental = 3.00
		
		oldVRent = self.oldVid.getNumber()
		newVRent = self.newVid.getNumber()
		totalRental = self.totalVid.getNumber()
		
		totalRental = (oldRental * oldVRent) + (newRental * newVRent)

		self.totalVid.setNumber(totalRental)

def main():
	'''instantiates and pops up the window.'''
	VhusVideo().mainloop()

#global call to main() funct
main() 