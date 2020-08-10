from tkinter import *
import time
import pickle

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
		self.varHeight.set(self.mainPage.currentUser.userHeight)
		self.varWeight = StringVar()
		self.varWeight.set('')

		self.labelHeight = Label(self.mainPage.application, text="Quelle est votre taille ?", font=self.mainPage.largeFont)
		self.labelHeight['bg'] = "#E3FBFA"
		self.labelHeight['fg'] = "#8000FF"

		self.entryHeight = Entry(self.mainPage.application, textvariable=self.varHeight, width=5, font=self.mainPage.normalInputFont)
		self.entryHeight.bind('<KeyRelease>', self.jumpToWeight)

		self.labelCentimeters = Label(self.mainPage.application, text="centimètres", font=self.mainPage.largeFont)
		self.labelCentimeters['bg'] = "#E3FBFA"
		self.labelCentimeters['fg'] = "#000000"

		self.labelWeight = Label(self.mainPage.application, text="Quel est votre poids ?", font=self.mainPage.largeFont)
		self.labelWeight['bg'] = "#E3FBFA"
		self.labelWeight['fg'] = "#8000FF"

		self.entryWeight = Entry(self.mainPage.application, textvariable=self.varWeight, width=5, font=self.mainPage.normalInputFont)
		self.entryWeight.bind('<KeyRelease>', self.jumpToCalculate)

		self.labelKilograms = Label(self.mainPage.application, text="kilogrammes", font=self.mainPage.largeFont)
		self.labelKilograms['bg'] = "#E3FBFA"
		self.labelKilograms['fg'] = "#000000"

		self.labelWarningConnexion = Label(self.mainPage.application, text="", font=self.mainPage.largeFont)
		self.labelWarningConnexion['bg'] = "#E3FBFA"
		self.labelWarningConnexion['fg'] = "#FF0000"

		self.buttonCalculate = Button(self.mainPage.application, text="Calculez votre IMC", font=self.mainPage.largeFont, width=30, command=self.calculateBMI)
		self.buttonCalculate['bg'] = "#3366FF"
		self.buttonCalculate['fg'] = "#FFFFFF"


		self.labelHeight.place(x=33, y=140)
		self.entryHeight.place(x=35, y=180)
		self.labelCentimeters.place(x=85, y=175)
		self.labelWeight.place(x=33, y=240)
		self.entryWeight.place(x=35, y=280)
		self.labelKilograms.place(x=85, y=275)
		self.labelWarningConnexion.place(x=35, y=310)
		self.buttonCalculate.place(x=80, y=355)

		self.entryHeight.focus()

	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		self.calculateBMI()

	def jumpToWeight(self, event):
		""" Automatic jump to the Weight aera when user enter 3 inputs """ 
		if len(self.entryHeight.get()) == 3:
			self.entryWeight.focus()

	def jumpToCalculate(self, event):
		""" Automatic jump to the Calculate button when user enter 5 inputs """ 
		if len(self.entryWeight.get()) == 5:
			self.buttonCalculate.focus()

	def calculateBMI(self):
		""" Calculate BMI and update profile """
		self.labelWarningConnexion.destroy()

		errorInputs = False
		controlHeight = ""
		controlWeight = ""

		try:
			controlHeight = int(self.varHeight.get())
		except:
			errorInputs = True
		else:
			if controlHeight < 30 or controlHeight > 300:
				errorInputs = True
		
		if errorInputs == True:
			self.labelWarningConnexion = Label(self.mainPage.application, text="Erreur sur votre taille (en centimètres)", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E3FBFA"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=35, y=310)
			self.entryHeight.focus()
		else:
			pointChange = self.varWeight.get()
			pointChange = pointChange.replace(",", ".")
			try:
				controlWeight = float(pointChange)
			except:
				errorInputs = True
			else:
				if controlWeight < 3 or controlWeight > 300:
					errorInputs = True

			if errorInputs == True:
				self.labelWarningConnexion = Label(self.mainPage.application, text="Erreur sur votre poids (en kilogrammes)", font=self.mainPage.largeFont)
				self.labelWarningConnexion['bg'] = "#E3FBFA"
				self.labelWarningConnexion['fg'] = "#FF0000"
				self.labelWarningConnexion.place(x=35, y=310)
				self.entryWeight.focus()
			else:
				BMI = controlWeight / ((controlHeight / 100) * (controlHeight / 100)) 
				currentTime = time.time()
				self.mainPage.currentBMI = BMI
				self.mainPage.currentUser.userHeight = controlHeight
				self.mainPage.currentUser.userWeight = controlWeight
				self.mainPage.currentUser.userBMI.append(BMI)
				self.mainPage.currentUser.lastVisits.append(currentTime)

				file = open("PyHealth_User/users", "rb")
				myUnplickler = pickle.Unpickler(file)
				usersList = []
				try:
					while True:
						usersList.append(myUnplickler.load())
				except:
					pass
				file.close()

				file = open("PyHealth_User/users", "wb")
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

				self.mainPage.changeHeightAndWeightToResults()
