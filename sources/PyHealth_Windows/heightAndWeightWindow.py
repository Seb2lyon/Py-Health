from tkinter import *


class heightAndWeightWindow:
	""" Insert to the Main window of the application
	This class display the form to fill the user's : 
	- height
	- weight
	and lauch the BMI calculation """

	def __init__(self, page):
		
		self.mainPage = page

		self.mainPage.application.bind('<KeyRelease-Return>', self.pressReturn)

		self.varHeight = IntVar()
		self.varHeight = self.mainPage.currentUser.userHeight
		self.varWeight = DoubleVar()
		self.varWeight = self.mainPage.currentUser.userWeight

		self.labelHeight = Label(self.mainPage.application, text="Quelle est votre taille ?", font=self.mainPage.largeFont)
		self.labelHeight['bg'] = "#E4E4E4"
		self.labelHeight['fg'] = "#993300"

		self.entryHeight = Entry(self.mainPage.application, textvariable=self.varHeight, width=4, font=self.mainPage.normalInputFont)

		self.labelCentimeters = Label(self.mainPage.application, text="centimètres", font=self.mainPage.largeFont)
		self.labelCentimeters['bg'] = "#E4E4E4"
		self.labelCentimeters['fg'] = "#000000"

		self.labelWeight = Label(self.mainPage.application, text="Quel est votre poids ?", font=self.mainPage.largeFont)
		self.labelWeight['bg'] = "#E4E4E4"
		self.labelWeight['fg'] = "#993300"

		self.entryWeight = Entry(self.mainPage.application, textvariable=self.varWeight, width=4, font=self.mainPage.normalInputFont)

		self.labelKilograms = Label(self.mainPage.application, text="kilogrammes", font=self.mainPage.largeFont)
		self.labelKilograms['bg'] = "#E4E4E4"
		self.labelKilograms['fg'] = "#000000"

		self.buttonCalculate = Button(self.mainPage.application, text="Calculez votre IMC", font=self.mainPage.largeFont, width=30, command=self.calculateBMI)
		self.buttonCalculate['bg'] = "#008000"
		self.buttonCalculate['fg'] = "#FFFFFF"


		self.labelHeight.place(x=33, y=140)
		self.entryHeight.place(x=35, y=180)
		self.labelCentimeters.place(x=80, y=175)
		self.labelWeight.place(x=33, y=240)
		self.entryWeight.place(x=35, y=280)
		self.labelKilograms.place(x=80, y=275)
		self.buttonCalculate.place(x=80, y=355)


	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		self.calculateBMI()

	def calculateBMI(self):
		""" Calculate BMI """
		pass
		# Calculate BMI


		# TODO : Verify inputs Height and Weight
		# TODO : Save Height and Weight in current user profile
		# TODO : Calculate BMI
