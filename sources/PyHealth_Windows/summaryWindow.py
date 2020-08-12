from tkinter import *
from tkinter.messagebox import *
import pickle

class summaryWindow:
	""" Insert to the Main window of the application
	This class display the summary of the user's attributes,
	then propose :
	- to confirm this datas
	- to modify this datas
	- to cancel this account """

	def __init__(self, page):
		
		self.mainPage = page

		self.mainPage.application.bind('<KeyRelease-Return>', self.pressReturn)

		welcomeString = "Bienvenue " + self.mainPage.currentUser.userFirstName + ","

		self.labelCheck1 = Label(self.mainPage.application, text=welcomeString, font=self.mainPage.largeFont)
		self.labelCheck1['bg'] = "#E3FBFA"
		self.labelCheck1['fg'] = "#000000"

		self.labelCheck2 = Label(self.mainPage.application, text="Merci de bien vouloir confirmer vos informations", font=self.mainPage.largeFont)
		self.labelCheck2['bg'] = "#E3FBFA"
		self.labelCheck2['fg'] = "#000000"

		self.labelCheck3 = Label(self.mainPage.application, text="personnelles : ", font=self.mainPage.largeFont)
		self.labelCheck3['bg'] = "#E3FBFA"
		self.labelCheck3['fg'] = "#000000"

		self.labelFirstName1 = Label(self.mainPage.application, text="Votre prénom est ", font=self.mainPage.largeFont)
		self.labelFirstName1['bg'] = "#E3FBFA"
		self.labelFirstName1['fg'] = "#8000FF"

		self.labelFirstName2 = Label(self.mainPage.application, text=self.mainPage.currentUser.userFirstName, font=self.mainPage.largeFont)
		self.labelFirstName2['bg'] = "#E3FBFA"
		self.labelFirstName2['fg'] = "#3366FF"

		birthDay = ""
		birthMonth = ""

		if self.mainPage.currentUser.userDayOfBirth < 10:
			birthDay = "0" + str(self.mainPage.currentUser.userDayOfBirth)
		else:
			birthDay = str(self.mainPage.currentUser.userDayOfBirth)

		if self.mainPage.currentUser.userMonthOfBirth < 10:
			birthMonth = "0" + str(self.mainPage.currentUser.userMonthOfBirth)
		else:
			birthMonth = str(self.mainPage.currentUser.userMonthOfBirth)

		birthDate = birthDay + "/" + birthMonth + "/" + str(self.mainPage.currentUser.userYearOfBirth)

		self.labelBirthDate2 = Label(self.mainPage.application, text=birthDate, font=self.mainPage.largeFont)

		if self.mainPage.currentUser.userGender == "F":
			self.labelGender1 = Label(self.mainPage.application, text="Vous êtes une ", font=self.mainPage.largeFont)
			self.labelGender2 = Label(self.mainPage.application, text="femme", font=self.mainPage.largeFont)
			self.labelBirthDate1 = Label(self.mainPage.application, text="Vous êtes née le", font=self.mainPage.largeFont)	
			self.labelGender2.place(x=165, y= 266)
			self.labelBirthDate2.place(x=186, y=297)
		else:
			self.labelGender1 = Label(self.mainPage.application, text="Vous êtes un ", font=self.mainPage.largeFont)
			self.labelGender2 = Label(self.mainPage.application, text="homme", font=self.mainPage.largeFont)
			self.labelBirthDate1 = Label(self.mainPage.application, text="Vous êtes né le", font=self.mainPage.largeFont)	
			self.labelGender2.place(x=155, y= 266)
			self.labelBirthDate2.place(x=176, y=297)

		self.labelGender1['bg'] = "#E3FBFA"
		self.labelGender1['fg'] = "#8000FF"	
		self.labelGender2['bg'] = "#E3FBFA"
		self.labelGender2['fg'] = "#3366FF"
		self.labelBirthDate1['bg'] = "#E3FBFA"
		self.labelBirthDate1['fg'] = "#8000FF"	
		self.labelBirthDate2['bg'] = "#E3FBFA"
		self.labelBirthDate2['fg'] = "#3366FF"

		self.buttonModify = Button(self.mainPage.application, text="Modifiez", font=self.mainPage.normalFont, width=10, command=self.modifyProfile)
		self.buttonModify['bg'] = "#969696"
		self.buttonModify['fg'] = "#FFFFFF"

		self.buttonConfirm = Button(self.mainPage.application, text="Confirmez", font=self.mainPage.normalFont, width=10, command=self.validateProfile)
		self.buttonConfirm['bg'] = "#969696"
		self.buttonConfirm['fg'] = "#FFFFFF"

		self.labelDeleteAccount = Label(self.mainPage.application, text="Supprimez votre compte", font=self.mainPage.normalLinkFont, cursor="hand2")
		self.labelDeleteAccount['bg'] = "#E3FBFA"
		self.labelDeleteAccount['fg'] = "#000000"
		self.labelDeleteAccount.bind("<Button-1>", lambda e: self.deleteAccountProcess())	

		self.labelCheck1.place(x=33, y=140)
		self.labelCheck2.place(x=33, y=163)
		self.labelCheck3.place(x=33, y=186)
		self.labelFirstName1.place(x=33, y=235)
		self.labelFirstName2.place(x=192, y=235)
		self.labelGender1.place(x=33, y=266)
		self.labelBirthDate1.place(x=33, y=297)
		self.buttonModify.place(x=57, y=354)
		self.buttonConfirm.place(x=329, y=354)
		self.labelDeleteAccount.place(x=150, y=415)


	def pressReturn(self, event):
		""" Manage the action when user press the key Enter """
		self.validateProfile()

	def modifyProfile(self):
		""" Go back to the Create account page 1 """
		self.mainPage.changeSummaryToCreateAccountOne()

	def deleteAccountProcess(self):
		""" Delete the account of the current user """
		cancelAnswer = askokcancel(title="Py Health - Supprimer le compte", message="Souhaitez-vous réellement supprimer votre compte \"Py Health\" ?")
		if cancelAnswer == True:
			file = open("config/users", "rb")
			myUnpickler = pickle.Unpickler(file)
			appUsers = []
			newAppUsers = []
			try:
				while True:
					oneUser = myUnpickler.load()
					appUsers.append(oneUser)
			except:
				pass
			file.close()

			nbrUsers = len(appUsers)
			i = 0
			while i < nbrUsers:
				if appUsers[i].userPseudo != self.mainPage.currentUser.userPseudo:
					newAppUsers.append(appUsers[i])
				i = i + 1

			file = open("config/users", "wb")
			myPickler = pickle.Pickler(file)
			nbrUsers = len(newAppUsers)
			i = 0
			while i < nbrUsers:
				myPickler.dump(newAppUsers[i])
				i = i + 1
			file.close()

			showinfo(title="Py Health - Compte supprimé", message="Votre compte \"Py Health\" a bien été supprimé !\nEn espérant vous revoir bientôt...")

			self.mainPage.changeSummaryToMain()

	def validateProfile(self):
		""" Continue to the Height and Weight page """
		self.mainPage.changeSummaryToHeightAndWeight()
