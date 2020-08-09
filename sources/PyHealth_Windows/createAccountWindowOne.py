from tkinter import *
from tkinter.font import *
import time
import datetime

class createAccountWindowOne:
	""" Insert to the Main window of the application
	This class provide the first part of the Creating account page structure
	- First name
	- Gender
	- Date of birth """

	def __init__(self, page):
		
		self.mainPage = page

		self.mainPage.application.bind('<KeyRelease-Return>', self.pressReturn)

		self.varFirstName = StringVar()
		self.varFirstName.set(self.mainPage.currentUser.userFirstName)

		self.labelFirstName = Label(self.mainPage.application, text="Votre prénom :", font=self.mainPage.largeFont)
		self.labelFirstName['bg'] = "#E4E4E4"
		self.labelFirstName['fg'] = "#993300"

		self.entryFirstName = Entry(self.mainPage.application, textvariable=self.varFirstName, width=55, font=self.mainPage.normalInputFont)

		self.labelGender = Label(self.mainPage.application, text="Vous êtes :", font=self.mainPage.largeFont)
		self.labelGender['bg'] = "#E4E4E4"
		self.labelGender['fg'] = "#993300"

		gender = ['une femme', 'un homme']
		valGender = ['F', 'H']
		self.varGender = StringVar()
		self.varGender.set(self.mainPage.currentUser.userGender)
		self.radioStock = []

		j = 220

		for i in range(2):
			self.radioGender = Radiobutton(self.mainPage.application, variable=self.varGender, text=gender[i], value=valGender[i], font=self.mainPage.largeFont)
			self.radioGender['bg'] = "#E4E4E4"
			self.radioGender['fg'] = "#000000"
			self.radioGender.place(x=140, y=j)
			self.radioStock.append(self.radioGender)
			j = j + 33

		self.labelBirthDate = Label(self.mainPage.application, text="Votre date de naissance :", font=self.mainPage.largeFont)
		self.labelBirthDate['bg'] = "#E4E4E4"
		self.labelBirthDate['fg'] = "#993300"

		self.varBirthDay = IntVar()
		self.varBirthMonth = IntVar()
		self.varBirthYear = IntVar()
		self.varBirthDay.set('')
		self.varBirthMonth.set('')
		self.varBirthYear.set('')

		self.jumpDay = 0

		self.entryBirthDay = Entry(self.mainPage.application, textvariable=self.varBirthDay, width=3, font=self.mainPage.normalInputFont)
		if self.mainPage.currentUser.userDayOfBirth == '':
			self.entryBirthDay.insert(0, 'JJ')
			self.entryBirthDay.config(fg = "grey")
		else:
			if self.mainPage.currentUser.userDayOfBirth < 10:
				self.entryBirthDay.insert(0, "0" + str(self.mainPage.currentUser.userDayOfBirth))
				self.entryBirthDay.config(fg = 'black')
			else:
				self.entryBirthDay.insert(0, self.mainPage.currentUser.userDayOfBirth)
				self.entryBirthDay.config(fg = 'black')
		self.entryBirthDay.bind('<FocusIn>', self.entryBirthDay_click)
		self.entryBirthDay.bind('<FocusOut>', self.entryBirthDay_focusout)
		self.entryBirthDay.bind('<KeyRelease>', self.jumpToMonth)

		self.labelSlash1 = Label(self.mainPage.application, text=" / ", font=self.mainPage.normalFont)
		self.labelSlash1['bg'] = "#E4E4E4"
		self.labelSlash1['fg'] = "#000000"

		self.entryBirthMonth = Entry(self.mainPage.application, textvariable=self.varBirthMonth, width=3, font=self.mainPage.normalInputFont)
		if self.mainPage.currentUser.userMonthOfBirth == '':
			self.entryBirthMonth.insert(0, 'MM')
			self.entryBirthMonth.config(fg = "grey")
		else:
			if self.mainPage.currentUser.userMonthOfBirth < 10:
				self.entryBirthMonth.insert(0, "0" + str(self.mainPage.currentUser.userMonthOfBirth))
				self.entryBirthMonth.config(fg = 'black')
			else:
				self.entryBirthMonth.insert(0, self.mainPage.currentUser.userMonthOfBirth)
				self.entryBirthMonth.config(fg = 'black')
		self.entryBirthMonth.bind('<FocusIn>', self.entryBirthMonth_click)
		self.entryBirthMonth.bind('<FocusOut>', self.entryBirthMonth_focusout)
		self.entryBirthMonth.bind('<KeyRelease>', self.jumpToYear)

		self.labelSlash2 = Label(self.mainPage.application, text=" / ", font=self.mainPage.normalFont)
		self.labelSlash2['bg'] = "#E4E4E4"
		self.labelSlash2['fg'] = "#000000"

		self.entryBirthYear = Entry(self.mainPage.application, textvariable=self.varBirthYear, width=5, font=self.mainPage.normalInputFont)
		if self.mainPage.currentUser.userYearOfBirth == '':
			self.entryBirthYear.insert(0, 'AAAA')
			self.entryBirthYear.config(fg = "grey")
		else:
			self.entryBirthYear.insert(0, self.mainPage.currentUser.userYearOfBirth)
			self.entryBirthYear.config(fg = 'black')
		self.entryBirthYear.bind('<FocusIn>', self.entryBirthYear_click)
		self.entryBirthYear.bind('<FocusOut>', self.entryBirthYear_focusout)
		self.entryBirthYear.bind('<KeyRelease>', self.jumpToNextButton)

		self.labelWarningConnexion = Label(self.mainPage.application, text="", font=self.mainPage.largeFont)
		self.labelWarningConnexion['bg'] = "#E4E4E4"
		self.labelWarningConnexion['fg'] = "#FF0000"

		self.buttonCancel = Button(self.mainPage.application, text="Annuler", font=self.mainPage.normalFont, width=10, command=self.cancelCreateAccount)
		self.buttonCancel['bg'] = "#969696"
		self.buttonCancel['fg'] = "#FFFFFF"

		self.buttonNext = Button(self.mainPage.application, text="Suivant", font=self.mainPage.normalFont, width=10, command=self.validateFirstPart)
		self.buttonNext['bg'] = "#969696"
		self.buttonNext['fg'] = "#FFFFFF"

		self.labelFirstName.place(x=25, y=144)
		self.entryFirstName.place(x=27, y=175)
		self.labelGender.place(x=25, y=222)
		self.labelBirthDate.place(x=25, y=298)
		self.entryBirthDay.place(x=27, y=330)
		self.labelSlash1.place(x=55, y=326)
		self.entryBirthMonth.place(x=77, y=330)
		self.labelSlash2.place(x=105, y=326)
		self.entryBirthYear.place(x=127, y=330)
		self.labelWarningConnexion.place(x=25, y=365)
		self.buttonCancel.place(x=57, y=404)
		self.buttonNext.place(x=329, y=404)

		self.entryFirstName.focus()


	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		self.validateFirstPart()

	def entryBirthDay_click(self, event):
		""" Wait for the user's input for Day """
		if self.entryBirthDay.get() == 'JJ':
			self.entryBirthDay.delete(0, 'end')
			self.entryBirthDay.insert(0, '')
			self.entryBirthDay.config(fg = 'black')

	def entryBirthDay_focusout(self, event):
		""" Display "JJ" by default in the place of birth Day """
		if self.entryBirthDay.get() == '':
	   		self.entryBirthDay.insert(0, 'JJ')
	   		self.entryBirthDay.config(fg = 'grey')

	def entryBirthMonth_click(self, event):
		""" Wait for the user's input for Month """
		if self.entryBirthMonth.get() == 'MM':
			self.entryBirthMonth.delete(0, 'end')
			self.entryBirthMonth.insert(0, '')
			self.entryBirthMonth.config(fg = 'black')

	def entryBirthMonth_focusout(self, event):
		""" Display "MM" by default in the place of birth Month """
		if self.entryBirthMonth.get() == '':
	   		self.entryBirthMonth.insert(0, 'MM')
	   		self.entryBirthMonth.config(fg = 'grey')

	def entryBirthYear_click(self, event):
		""" Wait for the user's input for Year """
		if self.entryBirthYear.get() == 'AAAA':
			self.entryBirthYear.delete(0, 'end')
			self.entryBirthYear.insert(0, '')
			self.entryBirthYear.config(fg = 'black')

	def entryBirthYear_focusout(self, event):
		""" Display "AAAA" by default in the place of birth Year """
		if self.entryBirthYear.get() == '':
			self.entryBirthYear.insert(0, 'AAAA')
			self.entryBirthYear.config(fg = 'grey')

	def jumpToMonth(self, event):
		""" Automatic jump to the Month aera when user enter 2 Day's inputs """ 
		if len(self.entryBirthDay.get()) == 2:
			self.entryBirthMonth.focus()

	def jumpToYear(self, event):
		""" Automatic jump to the Year aera when user enter 2 Month's inputs """ 
		if len(self.entryBirthMonth.get()) == 2:
			self.entryBirthYear.focus()

	def jumpToNextButton(self, event):
		""" Automatic jump to the Next button when user enter 4 Year's inputs """ 
		if len(self.entryBirthYear.get()) == 4:
			self.buttonNext.focus()

	def cancelCreateAccount(self):
		""" Cancel the creating account/modify account process """
		if self.mainPage.currentUser.userExist == False:
			self.mainPage.changeCreateAccountOneToMain()
		else:
			self.mainPage.changeCreateAccountOneToSummary()

	def validateFirstPart(self):
		""" Validate the inputs :
		- if the first name is not set : error message and retry
		- if the date of birth is not correct : error message and retry
		- if the date of bith is correct and first name set : go to the second part of the Creating account page """
		self.labelWarningConnexion.destroy()

		warningConnexion = False
		controlDay = ""
		controlMonth = ""
		controlYear = ""

		if self.varFirstName.get() == "":
			self.labelWarningConnexion = Label(self.mainPage.application, text="Veuillez renseigner votre prénom", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=25, y=365)
			self.entryFirstName.focus()
		else:
			if self.entryBirthDay.get() == "08":
				self.varBirthDay.set(8)

			if self.entryBirthDay.get() == "09":
				self.varBirthDay.set(9)

			if self.entryBirthMonth.get() == "08":
				self.varBirthMonth.set(8)

			if self.entryBirthMonth.get() == "09":
				self.varBirthMonth.set(9)

			try:
				controlDay = int(self.varBirthDay.get())
			except:
				warningConnexion = True
			else:
				if controlDay < 1 or controlDay > 31:
					warningConnexion = True

			try:
				controlMonth = int(self.varBirthMonth.get())
			except:
				warningConnexion = True
			else:
				if controlMonth < 1 or controlMonth > 12:
					warningConnexion = True

			try:
				controlYear = int(self.varBirthYear.get())
			except:
				warningConnexion = True
			else:
				if controlYear < 1900 or controlYear > int(time.strftime('%Y')):
					warningConnexion = True

			if warningConnexion == False:
				if controlMonth == 4 or controlMonth == 6 or controlMonth == 9 or controlMonth == 11:
					if controlDay == 31:
						warningConnexion = True

				if controlYear % 4 == 0:
					if controlYear % 100 == 0:
						if controlYear % 400 == 0:
							bisextile = True
						else:
							bisextile = False
					else:
						bisextile = True
				else:
					bisextile = False
				
				if controlMonth == 2 and bisextile == True:
					if controlDay > 29:
						warningConnexion = True
				elif controlMonth == 2 and bisextile == False:
					if controlDay > 28:
						warningConnexion = True

				if controlYear > 1969:
					currentTime = time.time()
					formatDate = str(controlDay) + "/" + str(controlMonth) + "/" + str(controlYear)
				
					try:
						result = time.mktime(datetime.datetime.strptime(formatDate, "%d/%m/%Y").timetuple())
					except ValueError:
						warningConnexion = True
					else:
						if result > currentTime:
							warningConnexion = True

			if warningConnexion:
				self.labelWarningConnexion = Label(self.mainPage.application, text="Date de naissance incorrecte", font=self.mainPage.largeFont)
				self.labelWarningConnexion['bg'] = "#E4E4E4"
				self.labelWarningConnexion['fg'] = "#FF0000"
				self.labelWarningConnexion.place(x=25, y=365)
				try:
					controlDay = int(self.varBirthDay.get())
				except:
					pass
				else:
					if controlDay < 10:
						self.entryBirthDay.delete(0, 'end')
						self.entryBirthDay.insert(0, "0" + str(controlDay))
						self.entryBirthDay.config(fg = 'black')
				try:
					controlMonth = int(self.varBirthMonth.get())
				except:
					pass
				else:
					if controlMonth < 10:
						self.entryBirthMonth.delete(0, 'end')
						self.entryBirthMonth.insert(0, "0" + str(controlMonth))
						self.entryBirthMonth.config(fg = 'black')
				self.entryBirthDay.focus()
			else:
				self.mainPage.currentUser.userFirstName = self.varFirstName.get()
				self.mainPage.currentUser.userGender = self.varGender.get()
				self.mainPage.currentUser.userDayOfBirth = self.varBirthDay.get()
				self.mainPage.currentUser.userMonthOfBirth = self.varBirthMonth.get()
				self.mainPage.currentUser.userYearOfBirth = self.varBirthYear.get()
				self.mainPage.changeCreateAccountOneToCreateAccountTwo()
