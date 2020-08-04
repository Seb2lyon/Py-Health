from tkinter import *
from tkinter.font import *

class welcomeWindow:
	""" Insert to the Main window of the application
	This class provide the Welcome page structure :
	- the credential form
	- the link to create a new account"""

	def __init__(self, page):

		self.mainPage = page

		self.imgSubTitle = PhotoImage(file="images/Sous-titre.gif")

		self.varID = StringVar()
		self.varPass = StringVar()

		self.subTitle = Label(self.mainPage.application, height=36, image=self.imgSubTitle)

		self.labelConnect = Label(self.mainPage.application, text="Connectez-vous à votre compte :", font=self.mainPage.largeFont)
		self.labelConnect['bg'] = "#E4E4E4"
		self.labelConnect['fg'] = "#993300"

		self.labelID = Label(self.mainPage.application, text="Identifiant :", font=self.mainPage.normalFont)
		self.labelID['bg'] = "#E4E4E4"
		self.labelID['fg'] = "#000000"

		self.entryID = Entry(self.mainPage.application, textvariable=self.varID, width=55, font=self.mainPage.normalInputFont)

		self.labelPass = Label(self.mainPage.application, text="Mot de passe :", font=self.mainPage.normalFont)
		self.labelPass['bg'] = "#E4E4E4"
		self.labelPass['fg'] = "#000000"

		self.entryPass = Entry(self.mainPage.application, textvariable=self.varPass, width=55, font=self.mainPage.normalInputFont, show="*")

		self.buttonConnect = Button(self.mainPage.application, text="Connexion", font=self.mainPage.normalFont)
		self.buttonConnect['bg'] = "#969696"
		self.buttonConnect['fg'] = "#FFFFFF"

		# self.warningConnexion = Label(self.mainPage.application, text="Identifiant et/ou mot de passe incorrect", font=self.largeFont)
		# self.warningConnexion['bg'] = "#E4E4E4"
		# self.warningConnexion['fg'] = "#FF0000"

		self.labelNoAccount = Label(self.mainPage.application, text="Vous n'avez pas de compte ?", font=self.mainPage.normalItalicFont)
		self.labelNoAccount['bg'] = "#E4E4E4"
		self.labelNoAccount['fg'] = "#000000"

		self.labelCreateAccount = Label(self.mainPage.application, text="Créez-le simplement", font=self.mainPage.normalLinkFont, cursor="hand2")
		self.labelCreateAccount['bg'] = "#E4E4E4"
		self.labelCreateAccount['fg'] = "#993300"
		self.labelCreateAccount.bind("<Button-1>", lambda e: self.mainPage.changeMainToCreateAccountOne())	

		self.subTitle.place(x=0, y=106)
		self.labelConnect.place(x=106, y=166)
		self.labelID.place(x=25, y=203)
		self.entryID.place(x=27, y=231)
		self.labelPass.place(x=25, y=267)
		self.entryPass.place(x=27, y=295)
		self.buttonConnect.place(x=192, y=330)
		# self.warningConnexion.place(x=71, y=375)
		self.labelNoAccount.place(x=30, y=416)
		self.labelCreateAccount.place(x=295, y=416)

		self.entryID.focus()
