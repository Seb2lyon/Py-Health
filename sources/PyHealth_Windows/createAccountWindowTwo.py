from tkinter import *

class createAccountWindowTwo:
	""" Insert to the Main window of the application
	This class provide the second part of the Creating account page structure
	- IS
	- Password
	- Confirm password """

	def __init__(self, page):
		
		self.mainPage = page

		self.varPseudo = StringVar()
		self.varPasswd1 = StringVar()
		self.varPasswd2 = StringVar()
		self.varPseudo.set("")
		self.varPasswd1.set("")
		self.varPasswd2.set("")

		self.labelPseudo = Label(self.mainPage.application, text="Votre identifiant :", font=self.mainPage.largeFont)
		self.labelPseudo['bg'] = "#E4E4E4"
		self.labelPseudo['fg'] = "#993300"

		self.entryPseudo = Entry(self.mainPage.application, textvariable=self.varPseudo, width=55, font=self.mainPage.normalInputFont)

		self.labelPasswd1 = Label(self.mainPage.application, text="Votre mot de passe :", font=self.mainPage.largeFont)
		self.labelPasswd1['bg'] = "#E4E4E4"
		self.labelPasswd1['fg'] = "#993300"

		self.entryPasswd1 = Entry(self.mainPage.application, textvariable=self.varPasswd1, width=55, font=self.mainPage.normalInputFont, show="*")

		self.labelPasswd2 = Label(self.mainPage.application, text="Confirmez votre mot de passe :", font=self.mainPage.largeFont)
		self.labelPasswd2['bg'] = "#E4E4E4"
		self.labelPasswd2['fg'] = "#993300"

		self.entryPasswd2 = Entry(self.mainPage.application, textvariable=self.varPasswd2, width=55, font=self.mainPage.normalInputFont, show="*")


		self.labelPseudo.place(x=25, y=144)
		self.entryPseudo.place(x=27, y=175)
		self.labelPasswd1.place(x=25, y=222)
		self.entryPasswd1.place(x=27, y=253)
		self.labelPasswd2.place(x=25, y=300)
		self.entryPasswd2.place(x=27, y=331)

		self.entryPseudo.focus()