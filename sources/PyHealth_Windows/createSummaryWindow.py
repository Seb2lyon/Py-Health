from tkinter import *

class createSummaryWindow:
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



		# TO BE CONTINUED



		self.labelCheck1.place(x=33, y=140)
		self.labelCheck2.place(x=33, y=163)
		self.labelCheck3.place(x=33, y=186)
