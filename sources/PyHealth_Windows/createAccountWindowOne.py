from tkinter import *
from tkinter.font import *

class createAccountWindowOne:
	""" Insert to the Main window of the application
	This class provide the first part of the Creating account page structure
	- First name
	- Gender
	- Date of birth"""

	def __init__(self, page):
		
		self.mainPage = page

		self.varFirstName = StringVar()

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
		self.varGender.set(valGender[0])

		j = 220

		for i in range(2):
			self.radioGender = Radiobutton(self.mainPage.application, variable=self.varGender, text=gender[i], value=valGender[i], font=self.mainPage.largeFont)
			self.radioGender['bg'] = "#E4E4E4"
			self.radioGender['fg'] = "#000000"
			self.radioGender.place(x=140, y=j)
			j = j + 33

		self.labelBirthDate = Label(self.mainPage.application, text="Votre date de naissance :", font=self.mainPage.largeFont)
		self.labelBirthDate['bg'] = "#E4E4E4"
		self.labelBirthDate['fg'] = "#993300"
		self.labelFirstName.place(x=25, y=144)
		self.entryFirstName.place(x=27, y=175)
		self.labelGender.place(x=25, y=222)
		self.labelBirthDate.place(x=25, y=298)

		self.entryFirstName.focus()