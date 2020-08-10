from tkinter import *

class resultsWindow:
	""" Insert to the Main window of the application
	This class display the results of the user's BMI : 
	- BMI index
	- BMI category
	- normal weight expected (if the user is not in a normal category)
	This class also has a link to the BMI Graph
	The close button is also here """

	def __init__(self, page):
		
		self.mainPage = page

		self.mainPage.application.bind('<KeyRelease-Return>', self.pressReturn)

	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		pass
