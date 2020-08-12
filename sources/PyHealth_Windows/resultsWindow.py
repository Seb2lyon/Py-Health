from tkinter import *
import time
from tkinter.messagebox import *
import pickle

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

		self.labelShowHistory = Label(self.mainPage.application, text="Consultez votre historique", font=self.mainPage.normalLinkFont, cursor="hand2")
		self.labelShowHistory['bg'] = "#E3FBFA"
		self.labelShowHistory['fg'] = "#8000FF"

		self.buttonQuit = Button(self.mainPage.application, text="Quitter", font=self.mainPage.normalFont, width=10, command=self.quitApp)
		self.buttonQuit['bg'] = "#969696"
		self.buttonQuit['fg'] = "#FFFFFF"
	

		self.labelBMI1.place(x=35, y=126)
		self.labelBMI2.place(x=200, y=126)
		self.labelResult.place(x=startPoint1, y=185)
		self.labelNormalWeight1.place(x=35, y=246)
		self.labelNormalWeight2.place(x=35, y=276)
		self.labelNormalWeight3.place(x=95, y=276)
		self.labelNormalWeight4.place(x=125, y=276)
		self.labelNormalWeight5.place(x=185, y=276)
		self.labelShowHistory.place(x=136, y=330)
		self.buttonQuit.place(x=190, y=380)


	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
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

	def userStateControl(self):
		""" Control the user state regarding his BMI, his sex and age (for children) """
		userState = ""
		stateColor = ""

		if self.userAge >= 18:
			if self.mainPage.currentBMI < 16.5:
				userState = "Vous êtes en état de dénutrition"
				stateColor = "#0000FF"
				self.createGraphPoints(0.0, 16.5, stateColor)
			elif self.mainPage.currentBMI >= 16.5 and self.mainPage.currentBMI < 18.5:
				userState = "Vous êtes en état de maigreur"
				stateColor = "#0000FF"
				self.createGraphPoints(16.5, 18.5, stateColor)
			elif self.mainPage.currentBMI >= 18.5 and self.mainPage.currentBMI < 25:
				userState = "Vous avez une corpulence normale"
				stateColor = "#01CA02"
				self.createGraphPoints(18.5, 25.0, stateColor)
			elif self.mainPage.currentBMI >= 25 and self.mainPage.currentBMI < 30:
				userState = "Vous êtes en surpoids"
				stateColor = "#FF6600"
				self.createGraphPoints(25.0, 30.0, stateColor)
			elif self.mainPage.currentBMI >= 30 and self.mainPage.currentBMI < 35:
				userState = "Vous êtes en état d'obésité modérée"
				stateColor = "#FF0000"
				self.createGraphPoints(30.0, 35.0, stateColor)
			elif self.mainPage.currentBMI >= 35 and self.mainPage.currentBMI < 40:
				userState = "Vous êtes en état d'obésité sévère"
				stateColor = "#FF0000"
				self.createGraphPoints(35.0, 40.0, stateColor)
			elif self.mainPage.currentBMI >= 40:
				userState = "Vous êtes en état d'obésité massive"
				stateColor = "#FF0000"
				self.createGraphPoints(40.0, 45.0, stateColor)

			minNormalWeight = 18.5 * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
			maxNormalWeight = 25 * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
			return userState, stateColor, minNormalWeight, maxNormalWeight

		else:

			if self.mainPage.currentUser.userGender == "H":

				boyBMI = {}
				boyBMI[1, 'minLow'] = 0.0
				boyBMI[1, 'maxLow'] = 15.0
				boyBMI[1, 'minNormal'] = 15.0 
				boyBMI[1, 'maxNormal'] = 20.5
				boyBMI[1, 'minHigh'] = 20.5
				boyBMI[1, 'maxHigh'] = 1000.0
				boyBMI[1, 'minXHigh'] = 1000.0
				boyBMI[1, 'maxXHigh'] = 1000.0
				boyBMI[2, 'minLow'] = 0.0
				boyBMI[2, 'maxLow'] = 14.5
				boyBMI[2, 'minNormal'] = 14.5 
				boyBMI[2, 'maxNormal'] = 19.0
				boyBMI[2, 'minHigh'] = 19.0
				boyBMI[2, 'maxHigh'] = 20.0
				boyBMI[2, 'minXHigh'] = 20.0
				boyBMI[2, 'maxXHigh'] = 1000.0
				boyBMI[3, 'minLow'] = 0.0
				boyBMI[3, 'maxLow'] = 14.0
				boyBMI[3, 'minNormal'] = 14.0 
				boyBMI[3, 'maxNormal'] = 18.5
				boyBMI[3, 'minHigh'] = 18.5
				boyBMI[3, 'maxHigh'] = 19.5
				boyBMI[3, 'minXHigh'] = 19.5
				boyBMI[3, 'maxXHigh'] = 1000.0
				boyBMI[4, 'minLow'] = 0.0
				boyBMI[4, 'maxLow'] = 13.75
				boyBMI[4, 'minNormal'] = 13.75 
				boyBMI[4, 'maxNormal'] = 18.0
				boyBMI[4, 'minHigh'] = 18.0
				boyBMI[4, 'maxHigh'] = 19.25
				boyBMI[4, 'minXHigh'] = 19.25
				boyBMI[4, 'maxXHigh'] = 1000.0
				boyBMI[5, 'minLow'] = 0.0
				boyBMI[5, 'maxLow'] = 13.5
				boyBMI[5, 'minNormal'] = 13.5 
				boyBMI[5, 'maxNormal'] = 18.0
				boyBMI[5, 'minHigh'] = 18.0
				boyBMI[5, 'maxHigh'] = 19.25
				boyBMI[5, 'minXHigh'] = 19.25
				boyBMI[5, 'maxXHigh'] = 1000.0
				boyBMI[6, 'minLow'] = 0.0
				boyBMI[6, 'maxLow'] = 13.5
				boyBMI[6, 'minNormal'] = 13.5 
				boyBMI[6, 'maxNormal'] = 18.0
				boyBMI[6, 'minHigh'] = 18.0
				boyBMI[6, 'maxHigh'] = 19.75
				boyBMI[6, 'minXHigh'] = 19.75
				boyBMI[6, 'maxXHigh'] = 1000.0
				boyBMI[7, 'minLow'] = 0.0
				boyBMI[7, 'maxLow'] = 13.5
				boyBMI[7, 'minNormal'] = 13.5 
				boyBMI[7, 'maxNormal'] = 18.25
				boyBMI[7, 'minHigh'] = 18.25
				boyBMI[7, 'maxHigh'] = 20.5
				boyBMI[7, 'minXHigh'] = 20.5
				boyBMI[7, 'maxXHigh'] = 1000.0
				boyBMI[8, 'minLow'] = 0.0
				boyBMI[8, 'maxLow'] = 13.5
				boyBMI[8, 'minNormal'] = 13.5 
				boyBMI[8, 'maxNormal'] = 18.75
				boyBMI[8, 'minHigh'] = 18.75
				boyBMI[8, 'maxHigh'] = 21.5
				boyBMI[8, 'minXHigh'] = 21.5
				boyBMI[8, 'maxXHigh'] = 1000.0
				boyBMI[9, 'minLow'] = 0.0
				boyBMI[9, 'maxLow'] = 13.5
				boyBMI[9, 'minNormal'] = 13.5 
				boyBMI[9, 'maxNormal'] = 19.25
				boyBMI[9, 'minHigh'] = 19.25
				boyBMI[9, 'maxHigh'] = 22.75
				boyBMI[9, 'minXHigh'] = 22.75
				boyBMI[9, 'maxXHigh'] = 1000.0
				boyBMI[10, 'minLow'] = 0.0
				boyBMI[10, 'maxLow'] = 13.75
				boyBMI[10, 'minNormal'] = 13.75 
				boyBMI[10, 'maxNormal'] = 20.0
				boyBMI[10, 'minHigh'] = 20.0
				boyBMI[10, 'maxHigh'] = 24.0
				boyBMI[10, 'minXHigh'] = 24.0
				boyBMI[10, 'maxXHigh'] = 1000.0
				boyBMI[11, 'minLow'] = 0.0
				boyBMI[11, 'maxLow'] = 14.0
				boyBMI[11, 'minNormal'] = 14.0 
				boyBMI[11, 'maxNormal'] = 20.5
				boyBMI[11, 'minHigh'] = 20.5
				boyBMI[11, 'maxHigh'] = 25.0
				boyBMI[11, 'minXHigh'] = 25.0
				boyBMI[11, 'maxXHigh'] = 1000.0
				boyBMI[12, 'minLow'] = 0.0
				boyBMI[12, 'maxLow'] = 14.25
				boyBMI[12, 'minNormal'] = 14.25 
				boyBMI[12, 'maxNormal'] = 21.5
				boyBMI[12, 'minHigh'] = 21.5
				boyBMI[12, 'maxHigh'] = 26.0
				boyBMI[12, 'minXHigh'] = 26.0
				boyBMI[12, 'maxXHigh'] = 1000.0
				boyBMI[13, 'minLow'] = 0.0
				boyBMI[13, 'maxLow'] = 14.75
				boyBMI[13, 'minNormal'] = 14.75 
				boyBMI[13, 'maxNormal'] = 22.25
				boyBMI[13, 'minHigh'] = 22.25
				boyBMI[13, 'maxHigh'] = 27.0
				boyBMI[13, 'minXHigh'] = 27.0
				boyBMI[13, 'maxXHigh'] = 1000.0
				boyBMI[14, 'minLow'] = 0.0
				boyBMI[14, 'maxLow'] = 15.25
				boyBMI[14, 'minNormal'] = 15.25 
				boyBMI[14, 'maxNormal'] = 23.25
				boyBMI[14, 'minHigh'] = 23.25
				boyBMI[14, 'maxHigh'] = 27.75
				boyBMI[14, 'minXHigh'] = 27.75
				boyBMI[14, 'maxXHigh'] = 1000.0
				boyBMI[15, 'minLow'] = 0.0
				boyBMI[15, 'maxLow'] = 15.75
				boyBMI[15, 'minNormal'] = 15.75
				boyBMI[15, 'maxNormal'] = 24.0
				boyBMI[15, 'minHigh'] = 24.0
				boyBMI[15, 'maxHigh'] = 28.25
				boyBMI[15, 'minXHigh'] = 28.25
				boyBMI[15, 'maxXHigh'] = 1000.0
				boyBMI[16, 'minLow'] = 0.0
				boyBMI[16, 'maxLow'] = 16.25
				boyBMI[16, 'minNormal'] = 16.25
				boyBMI[16, 'maxNormal'] = 25.0
				boyBMI[16, 'minHigh'] = 25.0
				boyBMI[16, 'maxHigh'] = 29.0
				boyBMI[16, 'minXHigh'] = 29.0
				boyBMI[16, 'maxXHigh'] = 1000.0
				boyBMI[17, 'minLow'] = 0.0
				boyBMI[17, 'maxLow'] = 16.75
				boyBMI[17, 'minNormal'] = 16.75 
				boyBMI[17, 'maxNormal'] = 25.5
				boyBMI[17, 'minHigh'] = 25.5
				boyBMI[17, 'maxHigh'] = 29.5
				boyBMI[17, 'minXHigh'] = 29.5
				boyBMI[17, 'maxXHigh'] = 1000.0

				if self.mainPage.currentBMI >= boyBMI[self.userAge, 'minLow'] and self.mainPage.currentBMI < boyBMI[self.userAge, 'maxLow']:
					userState = "Vous êtes en insuffisance pondérale"
					stateColor = "#0000FF"
					self.createGraphPoints(boyBMI[self.userAge, 'minLow'], boyBMI[self.userAge, 'maxLow'], stateColor)
				elif self.mainPage.currentBMI >= boyBMI[self.userAge, 'minNormal'] and self.mainPage.currentBMI < boyBMI[self.userAge, 'maxNormal']:
					userState = "Vous avez une corpulence normale"
					stateColor = "#01CA02"
					self.createGraphPoints(boyBMI[self.userAge, 'minNormal'], boyBMI[self.userAge, 'maxNormal'], stateColor)
				elif self.mainPage.currentBMI >= boyBMI[self.userAge, 'minHigh'] and self.mainPage.currentBMI < boyBMI[self.userAge, 'maxHigh']:
					userState = "Vous êtes en surpoids"
					stateColor = "#FF6600"
					self.createGraphPoints(boyBMI[self.userAge, 'minHigh'], boyBMI[self.userAge, 'maxHigh'], stateColor)
				elif self.mainPage.currentBMI >= boyBMI[self.userAge, 'minXHigh'] and self.mainPage.currentBMI < boyBMI[self.userAge, 'maxXHigh']:
					userState = "Vous êtes en état d'obésité"
					stateColor = "#FF0000"
					self.createGraphPoints(boyBMI[self.userAge, 'minXHigh'], 34.0, stateColor)

				minNormalWeight = boyBMI[self.userAge, 'minNormal'] * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
				maxNormalWeight = boyBMI[self.userAge, 'maxNormal'] * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
				return userState, stateColor, minNormalWeight, maxNormalWeight

			else:

				girlBMI = {}
				girlBMI[1, 'minLow'] = 0.0
				girlBMI[1, 'maxLow'] = 14.75
				girlBMI[1, 'minNormal'] = 14.75
				girlBMI[1, 'maxNormal'] = 20.0
				girlBMI[1, 'minHigh'] = 20.0
				girlBMI[1, 'maxHigh'] = 1000.0
				girlBMI[1, 'minXHigh'] = 1000.0
				girlBMI[1, 'maxXHigh'] = 1000.0
				girlBMI[2, 'minLow'] = 0.0
				girlBMI[2, 'maxLow'] = 14.25
				girlBMI[2, 'minNormal'] = 14.25 
				girlBMI[2, 'maxNormal'] = 19.0
				girlBMI[2, 'minHigh'] = 19.0
				girlBMI[2, 'maxHigh'] = 19.75
				girlBMI[2, 'minXHigh'] = 19.75
				girlBMI[2, 'maxXHigh'] = 1000.0
				girlBMI[3, 'minLow'] = 0.0
				girlBMI[3, 'maxLow'] = 13.75
				girlBMI[3, 'minNormal'] = 13.75 
				girlBMI[3, 'maxNormal'] = 18.5
				girlBMI[3, 'minHigh'] = 18.5
				girlBMI[3, 'maxHigh'] = 19.5
				girlBMI[3, 'minXHigh'] = 19.5
				girlBMI[3, 'maxXHigh'] = 1000.0
				girlBMI[4, 'minLow'] = 0.0
				girlBMI[4, 'maxLow'] = 13.5
				girlBMI[4, 'minNormal'] = 13.5 
				girlBMI[4, 'maxNormal'] = 18.0
				girlBMI[4, 'minHigh'] = 18.0
				girlBMI[4, 'maxHigh'] = 19.25
				girlBMI[4, 'minXHigh'] = 19.25
				girlBMI[4, 'maxXHigh'] = 1000.0
				girlBMI[5, 'minLow'] = 0.0
				girlBMI[5, 'maxLow'] = 13.0
				girlBMI[5, 'minNormal'] = 13.0 
				girlBMI[5, 'maxNormal'] = 17.75
				girlBMI[5, 'minHigh'] = 17.75
				girlBMI[5, 'maxHigh'] = 19.25
				girlBMI[5, 'minXHigh'] = 19.25
				girlBMI[5, 'maxXHigh'] = 1000.0
				girlBMI[6, 'minLow'] = 0.0
				girlBMI[6, 'maxLow'] = 13.0
				girlBMI[6, 'minNormal'] = 13.0 
				girlBMI[6, 'maxNormal'] = 17.75
				girlBMI[6, 'minHigh'] = 17.75
				girlBMI[6, 'maxHigh'] = 19.75
				girlBMI[6, 'minXHigh'] = 19.75
				girlBMI[6, 'maxXHigh'] = 1000.0
				girlBMI[7, 'minLow'] = 0.0
				girlBMI[7, 'maxLow'] = 13.0
				girlBMI[7, 'minNormal'] = 13.0 
				girlBMI[7, 'maxNormal'] = 18.0
				girlBMI[7, 'minHigh'] = 18.0
				girlBMI[7, 'maxHigh'] = 20.5
				girlBMI[7, 'minXHigh'] = 20.5
				girlBMI[7, 'maxXHigh'] = 1000.0
				girlBMI[8, 'minLow'] = 0.0
				girlBMI[8, 'maxLow'] = 13.0
				girlBMI[8, 'minNormal'] = 13.0 
				girlBMI[8, 'maxNormal'] = 18.5
				girlBMI[8, 'minHigh'] = 18.5
				girlBMI[8, 'maxHigh'] = 21.75
				girlBMI[8, 'minXHigh'] = 21.75
				girlBMI[8, 'maxXHigh'] = 1000.0
				girlBMI[9, 'minLow'] = 0.0
				girlBMI[9, 'maxLow'] = 13.25
				girlBMI[9, 'minNormal'] = 13.25 
				girlBMI[9, 'maxNormal'] = 19.0
				girlBMI[9, 'minHigh'] = 19.0
				girlBMI[9, 'maxHigh'] = 23.0
				girlBMI[9, 'minXHigh'] = 23.0
				girlBMI[9, 'maxXHigh'] = 1000.0
				girlBMI[10, 'minLow'] = 0.0
				girlBMI[10, 'maxLow'] = 13.5
				girlBMI[10, 'minNormal'] = 13.5 
				girlBMI[10, 'maxNormal'] = 20.0
				girlBMI[10, 'minHigh'] = 20.0
				girlBMI[10, 'maxHigh'] = 24.25
				girlBMI[10, 'minXHigh'] = 24.25
				girlBMI[10, 'maxXHigh'] = 1000.0
				girlBMI[11, 'minLow'] = 0.0
				girlBMI[11, 'maxLow'] = 13.75
				girlBMI[11, 'minNormal'] = 13.75 
				girlBMI[11, 'maxNormal'] = 21.0
				girlBMI[11, 'minHigh'] = 21.0
				girlBMI[11, 'maxHigh'] = 25.5
				girlBMI[11, 'minXHigh'] = 25.5
				girlBMI[11, 'maxXHigh'] = 1000.0
				girlBMI[12, 'minLow'] = 0.0
				girlBMI[12, 'maxLow'] = 14.25
				girlBMI[12, 'minNormal'] = 14.25 
				girlBMI[12, 'maxNormal'] = 22.0
				girlBMI[12, 'minHigh'] = 22.0
				girlBMI[12, 'maxHigh'] = 26.75
				girlBMI[12, 'minXHigh'] = 26.75
				girlBMI[12, 'maxXHigh'] = 1000.0
				girlBMI[13, 'minLow'] = 0.0
				girlBMI[13, 'maxLow'] = 14.75
				girlBMI[13, 'minNormal'] = 14.75 
				girlBMI[13, 'maxNormal'] = 23.0
				girlBMI[13, 'minHigh'] = 23.0
				girlBMI[13, 'maxHigh'] = 27.75
				girlBMI[13, 'minXHigh'] = 27.75
				girlBMI[13, 'maxXHigh'] = 1000.0
				girlBMI[14, 'minLow'] = 0.0
				girlBMI[14, 'maxLow'] = 15.25
				girlBMI[14, 'minNormal'] = 15.25 
				girlBMI[14, 'maxNormal'] = 24.25
				girlBMI[14, 'minHigh'] = 24.25
				girlBMI[14, 'maxHigh'] = 28.5
				girlBMI[14, 'minXHigh'] = 28.5
				girlBMI[14, 'maxXHigh'] = 1000.0
				girlBMI[15, 'minLow'] = 0.0
				girlBMI[15, 'maxLow'] = 15.75
				girlBMI[15, 'minNormal'] = 15.75
				girlBMI[15, 'maxNormal'] = 25.0
				girlBMI[15, 'minHigh'] = 25.0
				girlBMI[15, 'maxHigh'] = 29.25
				girlBMI[15, 'minXHigh'] = 29.25
				girlBMI[15, 'maxXHigh'] = 1000.0
				girlBMI[16, 'minLow'] = 0.0
				girlBMI[16, 'maxLow'] = 16.25
				girlBMI[16, 'minNormal'] = 16.25
				girlBMI[16, 'maxNormal'] = 25.75
				girlBMI[16, 'minHigh'] = 25.75
				girlBMI[16, 'maxHigh'] = 29.5
				girlBMI[16, 'minXHigh'] = 29.5
				girlBMI[16, 'maxXHigh'] = 1000.0
				girlBMI[17, 'minLow'] = 0.0
				girlBMI[17, 'maxLow'] = 16.5
				girlBMI[17, 'minNormal'] = 16.5 
				girlBMI[17, 'maxNormal'] = 26.0
				girlBMI[17, 'minHigh'] = 26.0
				girlBMI[17, 'maxHigh'] = 29.75
				girlBMI[17, 'minXHigh'] = 29.75
				girlBMI[17, 'maxXHigh'] = 1000.0

				if self.mainPage.currentBMI >= girlBMI[self.userAge, 'minLow'] and self.mainPage.currentBMI < girlBMI[self.userAge, 'maxLow']:
					userState = "Vous êtes en insuffisance pondérale"
					stateColor = "#0000FF"
					self.createGraphPoints(girlBMI[self.userAge, 'minLow'], girlBMI[self.userAge, 'maxLow'], stateColor)
				elif self.mainPage.currentBMI >= girlBMI[self.userAge, 'minNormal'] and self.mainPage.currentBMI < girlBMI[self.userAge, 'maxNormal']:
					userState = "Vous avez une corpulence normale"
					stateColor = "#01CA02"
					self.createGraphPoints(girlBMI[self.userAge, 'minNormal'], girlBMI[self.userAge, 'maxNormal'], stateColor)
				elif self.mainPage.currentBMI >= girlBMI[self.userAge, 'minHigh'] and self.mainPage.currentBMI < girlBMI[self.userAge, 'maxHigh']:
					userState = "Vous êtes en surpoids"
					stateColor = "#FF6600"
					self.createGraphPoints(girlBMI[self.userAge, 'minHigh'], girlBMI[self.userAge, 'maxHigh'], stateColor)
				elif self.mainPage.currentBMI >= girlBMI[self.userAge, 'minXHigh'] and self.mainPage.currentBMI < girlBMI[self.userAge, 'maxXHigh']:
					userState = "Vous êtes en état d'obésité"
					stateColor = "#FF0000"
					self.createGraphPoints(girlBMI[self.userAge, 'minXHigh'], 34.0, stateColor)

				minNormalWeight = girlBMI[self.userAge, 'minNormal'] * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
				maxNormalWeight = girlBMI[self.userAge, 'maxNormal'] * (self.mainPage.currentUser.userHeight / 100) * (self.mainPage.currentUser.userHeight / 100)
				return userState, stateColor, minNormalWeight, maxNormalWeight

	def createGraphPoints(self, minBMI, maxBMI, colorStatus):
		""" Create the point coordinate for the history graph """
		if colorStatus == "#0000FF":
			minCoordinate = 180
			maxCoordinate = 240
		elif colorStatus == "#01CA02":
			minCoordinate = 120
			maxCoordinate = 180
		elif colorStatus == "#FF6600":
			minCoordinate = 60
			maxCoordinate = 120
		elif colorStatus == "#FF0000":
			minCoordinate = 0
			maxCoordinate = 60

		modCurrentBMI = 0.0
		if self.mainPage.currentBMI > maxBMI:
			modCurrentBMI = maxBMI
		else:
			modCurrentBMI = self.mainPage.currentBMI

		BMIDelta = maxBMI - minBMI
		BMIDev = modCurrentBMI - minBMI

		percentBMI = (100 * BMIDev) / BMIDelta

		graphDelta = maxCoordinate - minCoordinate

		percentGraph = (graphDelta * percentBMI) / 100

		coordinatePoint = maxCoordinate - percentGraph
		coordinatePoint = int(coordinatePoint)

		self.mainPage.currentUser.coordinatePoints.append(coordinatePoint)

		if len(self.mainPage.currentUser.coordinatePoints) > 10:
			del self.mainPage.currentUser.userBMI[0] 
			del self.mainPage.currentUser.lastVisits[0]
			del self.mainPage.currentUser.coordinatePoints[0]

	def quitApp(self):
		""" Close the app """
		quitAnswer = askokcancel(title="Py Health - Quitter l'application", message="Souhaitez-vous réellement quitter l'application \"Py Health\" ?")
		if quitAnswer == True:

			file = open("config/users", "rb")
			myUnplickler = pickle.Unpickler(file)
			usersList = []
			try:
				while True:
					usersList.append(myUnplickler.load())
			except:
				pass
			file.close()

			file = open("config/users", "wb")
			myPickler = pickle.Pickler(file)
			usersNumber = len(usersList)
			i = 0
			while i < usersNumber:
				if usersList[i].userPseudo == self.mainPage.currentUser.userPseudo:
					usersList[i] = self.mainPage.currentUser
					myPickler.dump(usersList[i])
				else:
					myPickler.dump(usersList[i])
				i = i + 1
			file.close()
	
			self.mainPage.application.quit()


		# TODO : Add congratulation if the BMI is normal (adult + children)
		# TODO : Manage 0 year (too young)

		# TO BE CONTINED : Link to history
