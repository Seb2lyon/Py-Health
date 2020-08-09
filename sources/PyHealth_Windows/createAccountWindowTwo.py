from tkinter import *
from tkinter.messagebox import *
import pickle
import hashlib

class createAccountWindowTwo:
	""" Insert to the Main window of the application
	This class provide the second part of the Creating account page structure
	- IS
	- Password
	- Confirm password """

	def __init__(self, page):
		
		self.mainPage = page

		self.mainPage.application.bind('<KeyRelease-Return>', self.pressReturn)

		self.varPseudo = StringVar()
		self.varPasswd1 = StringVar()
		self.varPasswd2 = StringVar()
		self.varPseudo.set(self.mainPage.currentUser.userPseudo)
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

		self.labelWarningConnexion = Label(self.mainPage.application, text="", font=self.mainPage.largeFont)
		self.labelWarningConnexion['bg'] = "#E4E4E4"
		self.labelWarningConnexion['fg'] = "#FF0000"

		self.buttonPrevious = Button(self.mainPage.application, text="Précédent", font=self.mainPage.normalFont, width=10, command=self.goBackPageOne)
		self.buttonPrevious['bg'] = "#969696"
		self.buttonPrevious['fg'] = "#FFFFFF"

		self.buttonValidate = Button(self.mainPage.application, text="Validez", font=self.mainPage.normalFont, width=10, command=self.validateSecondPart)
		self.buttonValidate['bg'] = "#969696"
		self.buttonValidate['fg'] = "#FFFFFF"

		self.labelPseudo.place(x=25, y=144)
		self.entryPseudo.place(x=27, y=175)
		self.labelPasswd1.place(x=25, y=222)
		self.entryPasswd1.place(x=27, y=253)
		self.labelPasswd2.place(x=25, y=300)
		self.entryPasswd2.place(x=27, y=331)
		self.labelWarningConnexion.place(x=25, y=360)
		self.buttonPrevious.place(x=57, y=404)
		self.buttonValidate.place(x=329, y=404)

		self.entryPseudo.focus()


	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		self.validateSecondPart()

	def goBackPageOne(self):
		""" Go back to the Create account page 1 """
		self.mainPage.changeCreateAccountTwoToCreateAccountOne()

	def validateSecondPart(self):
		""" Validate the inputs :
		- if the pseudo is not set : error message and retry
		- if the pseudo is already taken : error message and retry
		- if the password is not set : error message and retry
		- if the password control is not set : error message and retry
		- if the 2 password inputs are different : error message and retry
		- if the pseudo and password are corrects : validate the account and record it """
		self.labelWarningConnexion.destroy()
		self.pseudoExist = False

		file = open("PyHealth_User/users", "rb")
		myUnplickler = pickle.Unpickler(file)

		try:
			while True:
				userExtract = myUnplickler.load()
				if userExtract.userPseudo.upper() == self.varPseudo.get().upper():
					self.pseudoExist = True
		except:
			pass

		file.close()

		if self.varPseudo.get() == '':
			self.labelWarningConnexion = Label(self.mainPage.application, text="Veuillez renseigner un identifiant", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=25, y=360)
			self.entryPseudo.focus()
		elif self.pseudoExist == True and self.mainPage.currentUser.userExist == False:
			self.labelWarningConnexion = Label(self.mainPage.application, text="Cet identifiant est déjà pris.", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=25, y=360)
			self.entryPseudo.focus()
		elif self.varPasswd1.get() == '':
			self.labelWarningConnexion = Label(self.mainPage.application, text="Veuillez renseigner un mot de passe", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=25, y=360)
			self.entryPasswd1.focus()
		elif self.varPasswd2.get() == '':
			self.labelWarningConnexion = Label(self.mainPage.application, text="Veuillez confirmer votre mot de passe", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=25, y=360)
			self.entryPasswd2.focus()
		elif self.varPasswd1.get() != self.varPasswd2.get():
			self.labelWarningConnexion = Label(self.mainPage.application, text="Mot de passe différent", font=self.mainPage.largeFont)
			self.labelWarningConnexion['bg'] = "#E4E4E4"
			self.labelWarningConnexion['fg'] = "#FF0000"
			self.labelWarningConnexion.place(x=25, y=360)
			self.entryPasswd1.focus()
		else:
			userPassword = self.varPasswd1.get()
			userPassword = userPassword.encode()
			hashedPassword = hashlib.sha1(userPassword).hexdigest()

			self.mainPage.currentUser.userPseudo = self.varPseudo.get()
			self.mainPage.currentUser.userPasswd = hashedPassword
			if self.mainPage.currentUser.userExist == True:
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

				showinfo(title="Py Health - Compte mis à jour", message="Félicitations!\nVotre compte \"Py Health\" a bien été mis à jour...")
			
			else:
				self.mainPage.currentUser.userExist = True
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
					myPickler.dump(usersList[i])
					i = i + 1
				myPickler.dump(self.mainPage.currentUser)
				file.close()

				showinfo(title="Py Health - Compte créé", message="Félicitations!\nVotre compte \"Py Health\" a été créé avec succès...")
				
			self.mainPage.changeCreateAccountTwoToSummary()
