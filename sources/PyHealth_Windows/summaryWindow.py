from tkinter import *

class summaryWindow:
	""" Insert to the Main window of the application
	This class display the summary of the user's attributes,
	then propose :
	- to confirm this datas
	- to modify this datas
	- to cancel this account """

	def __init__(self, page):
		
		self.mainPage = page

		welcomeString = "Bienvenue " + self.mainPage.currentUser.userFirstName + ","

		self.labelCheck1 = Label(self.mainPage.application, text=welcomeString, font=self.mainPage.largeFont)
		self.labelCheck1['bg'] = "#E4E4E4"
		self.labelCheck1['fg'] = "#000000"

		self.labelCheck2 = Label(self.mainPage.application, text="Merci de bien vouloir confirmer vos informations", font=self.mainPage.largeFont)
		self.labelCheck2['bg'] = "#E4E4E4"
		self.labelCheck2['fg'] = "#000000"

		self.labelCheck3 = Label(self.mainPage.application, text="personnelles : ", font=self.mainPage.largeFont)
		self.labelCheck3['bg'] = "#E4E4E4"
		self.labelCheck3['fg'] = "#000000"

		self.labelFirstName1 = Label(self.mainPage.application, text="Votre prénom est ", font=self.mainPage.largeFont)
		self.labelFirstName1['bg'] = "#E4E4E4"
		self.labelFirstName1['fg'] = "#993300"

		self.labelFirstName2 = Label(self.mainPage.application, text=self.mainPage.currentUser.userFirstName, font=self.mainPage.largeFont)
		self.labelFirstName2['bg'] = "#E4E4E4"
		self.labelFirstName2['fg'] = "#008000"

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
			self.labelBirthDate1 = Label(self.mainPage.application, text="Vous êtes née le ", font=self.mainPage.largeFont)	
			self.labelGender2.place(x=165, y= 266)
			self.labelBirthDate2.place(x=186, y=297)
		else:
			self.labelGender1 = Label(self.mainPage.application, text="Vous êtes un ", font=self.mainPage.largeFont)
			self.labelGender2 = Label(self.mainPage.application, text="homme", font=self.mainPage.largeFont)
			self.labelBirthDate1 = Label(self.mainPage.application, text="Vous êtes né le ", font=self.mainPage.largeFont)	
			self.labelGender2.place(x=155, y= 266)
			self.labelBirthDate2.place(x=176, y=297)

		self.labelGender1['bg'] = "#E4E4E4"
		self.labelGender1['fg'] = "#993300"	
		self.labelGender2['bg'] = "#E4E4E4"
		self.labelGender2['fg'] = "#008000"
		self.labelBirthDate1['bg'] = "#E4E4E4"
		self.labelBirthDate1['fg'] = "#993300"	
		self.labelBirthDate2['bg'] = "#E4E4E4"
		self.labelBirthDate2['fg'] = "#008000"






		# TO BE CONTINUED






		self.labelCheck1.place(x=33, y=140)
		self.labelCheck2.place(x=33, y=163)
		self.labelCheck3.place(x=33, y=186)
		self.labelFirstName1.place(x=33, y=235)
		self.labelFirstName2.place(x=192, y=235)
		self.labelGender1.place(x=33, y=266)
		self.labelBirthDate1.place(x=33, y=297)
