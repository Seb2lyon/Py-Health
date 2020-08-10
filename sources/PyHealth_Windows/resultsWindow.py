from tkinter import *
import time

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

		self.userAge = self.userAgeControl()

		self.labelBMI1 = Label(self.mainPage.application, text="Votre IMC est de :", font=self.mainPage.largeFont)
		self.labelBMI1['bg'] = "#E3FBFA"
		self.labelBMI1['fg'] = "#000000"

		self.labelBMI2 = Label(self.mainPage.application, text=round(self.mainPage.currentBMI, 2), font=self.mainPage.largeFont)
		self.labelBMI2['bg'] = "#E3FBFA"
		self.labelBMI2['fg'] = "#8000FF"

		showUserState, showStateColor, showMinNormalWeight, showMaxNormalWeight = self.userStateControl()
		stateSize = len(showUserState) * 12
		startPoint1 = 255 - (stateSize / 2)

		self.labelResult = Label(self.mainPage.application, text=showUserState, font=self.mainPage.xlargeFont)
		self.labelResult['bg'] = "#E3FBFA"
		self.labelResult['fg'] = showStateColor

		self.labelNormalWeight1 = Label(self.mainPage.application, text="Votre poids idéal est compris entre", font=self.mainPage.largeFont)
		self.labelNormalWeight1['bg'] = "#E3FBFA"
		self.labelNormalWeight1['fg'] = "#000000"

		self.labelNormalWeight2 = Label(self.mainPage.application, text=round(showMinNormalWeight, 1), font=self.mainPage.largeFont)
		self.labelNormalWeight2['bg'] = "#E3FBFA"
		self.labelNormalWeight2['fg'] = "#3366FF"

		self.labelNormalWeight3 = Label(self.mainPage.application, text="et", font=self.mainPage.largeFont)
		self.labelNormalWeight3['bg'] = "#E3FBFA"
		self.labelNormalWeight3['fg'] = "#000000"

		self.labelNormalWeight4 = Label(self.mainPage.application, text=round(showMaxNormalWeight, 1), font=self.mainPage.largeFont)
		self.labelNormalWeight4['bg'] = "#E3FBFA"
		self.labelNormalWeight4['fg'] = "#3366FF"

		self.labelNormalWeight5 = Label(self.mainPage.application, text="kilogrammes.", font=self.mainPage.largeFont)
		self.labelNormalWeight5['bg'] = "#E3FBFA"
		self.labelNormalWeight5['fg'] = "#000000"

		self.labelBMI1.place(x=35, y=126)
		self.labelBMI2.place(x=200, y=126)
		self.labelResult.place(x=startPoint1, y=185)
		self.labelNormalWeight1.place(x=35, y=246)
		self.labelNormalWeight2.place(x=35, y=276)
		self.labelNormalWeight3.place(x=95, y=276)
		self.labelNormalWeight4.place(x=125, y=276)
		self.labelNormalWeight5.place(x=185, y=276)


	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		pass

	def userStateControl(self):
		""" Control the user state regarding his BMI, his sex and age (for children) """
		userState = ""
		stateColor = ""

		if self.userAge >= 18:
			if self.mainPage.currentBMI < 16.5:
				userState = "Vous êtes en état de dénutrition"
				stateColor = "#0000FF"
			elif self.mainPage.currentBMI >= 16.5 and self.mainPage.currentBMI < 18.5:
				userState = "Vous êtes en état de maigreur"
				stateColor = "#0000FF"
			elif self.mainPage.currentBMI >= 18.5 and self.mainPage.currentBMI < 25:
				userState = "Vous avez une corpulence normale"
				stateColor = "#01CA02"
			elif self.mainPage.currentBMI >= 25 and self.mainPage.currentBMI < 30:
				userState = "Vous êtes en surpoids"
				stateColor = "#FF6600"
			elif self.mainPage.currentBMI >= 30 and self.mainPage.currentBMI < 35:
				userState = "Vous êtes en état d'obésité modérée"
				stateColor = "#FF0000"
			elif self.mainPage.currentBMI >= 35 and self.mainPage.currentBMI < 40:
				userState = "Vous êtes en état d'obésité sévère"
				stateColor = "#FF0000"
			elif self.mainPage.currentBMI >= 40:
				userState = "Vous êtes en état d'obésité massive"
				stateColor = "#FF0000"

			minNormalWeight = 18.5 * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
			maxNormalWeight = 25 * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
			return userState, stateColor, minNormalWeight, maxNormalWeight

		else:
			if self.mainPage.currentUser.userGender == "H":
				# Manage the boy status
				pass
			else:
				# Manage the girl status
				pass
				
	def userAgeControl(self):
		""" Control the actual age of the user """
		if self.mainPage.currentUser.userYearOfBirth == int(time.strftime('%Y')):
			userAgeCalculate = 0
		else:
			if self.mainPage.currentUser.userMonthOfBirth < int(time.strftime('%m')):
				userAgeCalculate = int(time.strftime('%Y')) - self.mainPage.currentUser.userYearOfBirth
			elif self.mainPage.currentUser.userMonthOfBirth > int(time.strftime('%m')):
				userAgeCalculate = int(time.strftime('%Y')) - self.mainPage.currentUser.userYearOfBirth - 1
			else:
				if self.mainPage.currentUser.userDayOfBirth <= int(time.strftime('%d')):
					userAgeCalculate = int(time.strftime('%Y')) - self.mainPage.currentUser.userYearOfBirth
				else:
					userAgeCalculate = int(time.strftime('%Y')) - self.mainPage.currentUser.userYearOfBirth - 1

		return userAgeCalculate


		# ADD CHILDREN CONTROL

		# TODO : Add congratulation if the BMI is normal

		# TO BE CONTINED
