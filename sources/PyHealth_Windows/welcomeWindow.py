from tkinter import *
from tkinter.font import *
import pickle
import hashlib

class welcomeWindow:
	""" Insert to the Main window of the application
	This class provide the Welcome page structure :
	- the credential form
	- the link to create a new account"""

	def __init__(self, page):

		self.mainPage = page

		self.mainPage.application.bind('<KeyRelease-Return>', self.pressReturn)

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

		self.buttonConnect = Button(self.mainPage.application, text="Connexion", font=self.mainPage.normalFont, width=10, command=self.checkCredentials)
		self.buttonConnect['bg'] = "#969696"
		self.buttonConnect['fg'] = "#FFFFFF"
		self.labelWarningConnexion = Label(self.mainPage.application, text="", font=self.mainPage.largeFont)
		self.labelWarningConnexion['bg'] = "#E4E4E4"
		self.labelWarningConnexion['fg'] = "#FF0000"

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
		self.buttonConnect.place(x=190, y=330)
		self.labelWarningConnexion.place(x=30, y=380)
		self.labelNoAccount.place(x=30, y=416)
		self.labelCreateAccount.place(x=295, y=416)

		self.entryID.focus()
		

	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		self.checkCredentials()

	def checkCredentials(self):
		""" Function that permit to chek the credentials
		- if the user exist in the users' list file : create current user and go to the summary page
		- if the user did not exist in the users' file : warning message """
		self.labelWarningConnexion.destroy()

		if self.entryID.get() == "":
			self.labelWarningConnexion = Label(self.mainPage.application, text="Identifiant obligatoire", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=30, y=380)
			self.entryID.focus()

		elif self.entryPass.get() == "":
			self.labelWarningConnexion = Label(self.mainPage.application, text="Mot de passe obligatoire", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=30, y=380)
			self.entryPass.focus()

		else:
			file = open("PyHealth_User/users", "rb")
			myUnpickler = pickle.Unpickler(file)
			appUsers = []

			try:
				while True:
					oneUser = myUnpickler.load()
					appUsers.append(oneUser)
			except:
				pass

			file.close()

			nbrUsers = len(appUsers)

			userExist = False

			i = 0

			inputPassword = self.varPass.get()
			inputPassword = inputPassword.encode()
			hashedPassword = hashlib.sha1(inputPassword).hexdigest()

			while i < nbrUsers:
				if appUsers[i].userPseudo.upper() == self.entryID.get().upper() and appUsers[i].userPasswd == hashedPassword:
					userExist = True
					self.mainPage.currentUser = appUsers[i]
				i = i + 1

			if userExist:
				self.mainPage.changeMainToSummary()	
			else:
				self.labelWarningConnexion = Label(self.mainPage.application, text="Identifiant et/ou mot de passe incorrect", font=self.mainPage.largeFont)
				self.labelWarningConnexion['bg'] = "#E4E4E4"
				self.labelWarningConnexion['fg'] = "#FF0000"
				self.labelWarningConnexion.place(x=30, y=380)
				self.entryID.focus()
