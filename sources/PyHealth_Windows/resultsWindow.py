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

		self.labelBMI1 = Label(self.mainPage.application, text="Votre IMC est de :", font=self.mainPage.largeFont)
		self.labelBMI1['bg'] = "#E4E4E4"
		self.labelBMI1['fg'] = "#000000"

		self.labelBMI2 = Label(self.mainPage.application, text=round(self.mainPage.currentBMI, 2), font=self.mainPage.largeFont)
		self.labelBMI2['bg'] = "#E4E4E4"
		self.labelBMI2['fg'] = "#993300"

		showUserState, showStateColor = self.userStateControl()
		stateSize = len(showUserState) * 12
		startPoint = 255 - (stateSize / 2)

		self.labelResult = Label(self.mainPage.application, text=showUserState, font=self.mainPage.xlargeFont)
		self.labelResult['bg'] = "#E4E4E4"
		self.labelResult['fg'] = showStateColor

		self.labelBMI1.place(x=35, y=126)
		self.labelBMI2.place(x=200, y=126)
		self.labelResult.place(x=startPoint, y=185)


	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		pass

	def userStateControl(self):
		""" Control the user state regarding his BMI, his sex and age (for children) """
		userState = ""
		stateColor = ""
		# ONLY FOR ADULTS
		if self.mainPage.currentBMI < 16.5:
			userState = "Vous êtes en état de dénutrition"
			stateColor = "#0000FF"
			return userState, stateColor
		elif self.mainPage.currentBMI >= 16.5 and self.mainPage.currentBMI < 18.5:
			userState = "Vous êtes en état de maigreur"
			stateColor = "#0000FF"
			return userState, stateColor
		elif self.mainPage.currentBMI >= 18.5 and self.mainPage.currentBMI < 25:
			userState = "Vous avez une corpulence normale"
			stateColor = "#01CA02"
			return userState, stateColor
		elif self.mainPage.currentBMI >= 25 and self.mainPage.currentBMI < 30:
			userState = "Vous êtes en surpoids"
			stateColor = "#FF6600"
			return userState, stateColor
		elif self.mainPage.currentBMI >= 30 and self.mainPage.currentBMI < 35:
			userState = "Vous êtes en état d'obésité modérée"
			stateColor = "#FF0000"
			return userState, stateColor
		elif self.mainPage.currentBMI >= 35 and self.mainPage.currentBMI < 40:
			userState = "Vous êtes en état d'obésité sévère"
			stateColor = "#FF0000"
			return userState, stateColor
		elif self.mainPage.currentBMI >= 40:
			userState = "Vous êtes en état d'obésité massive"
			stateColor = "#FF0000"
			return userState, stateColor

		# ADD CHILDREN CONTROL

		# TODO : Add congratulation if the BMI is normal

		# TO BE CONTINED
