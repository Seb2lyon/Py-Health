import webbrowser
from PyHealth_User.userClass import *
from PyHealth_Windows.welcomeWindow import *
from PyHealth_Windows.createAccountWindowOne import *
from PyHealth_Windows.createAccountWindowTwo import *
from PyHealth_Windows.summaryWindow import *
from PyHealth_Windows.heightAndWeightWindow import *
from PyHealth_Windows.resultsWindow import *
from PyHealth_Windows.historyWindow import *

class mainWindow(Frame):
	""" Main window : manager of the application
	This class provide the frame structure (banner and footer)
	and manage the hyperlink"""

	def __init__(self, app):
		Frame.__init__(self, app)
		self.application = app

		self.application.title("Py Health - Calculez votre IMC")
		self.application.iconphoto(True, PhotoImage(file="images/icon.png"))
		self.application.geometry("500x500")
		self.application.resizable(False, False)
		self.application['bg'] = "#E3FBFA"

		self.gridNormalFont = Font(family="Arial", size=8)
		self.gridBoldFont = Font(family="Arial", size=8, weight='bold')
		self.smallFont = Font(family="Arial Black", size=10)
		self.smallLinkFont = Font(family="Arial Black", size=10, underline=1)
		self.normalFont = Font(family="Arial Black", size=11)
		self.normalItalicFont = Font(family="Arial Black", size=11, slant="italic")
		self.normalLinkFont = Font(family="Arial Black", size=11, underline=1)
		self.normalInputFont = Font(family="Arial", size=11)
		self.largeFont = Font(family="Arial Black", size=12)
		self.largeUnderlineFont = Font(family="Arial Black", size=12, underline=1)
		self.xlargeFont = Font(family="Arial Black", size=15)

		self.currentUser = userClass()
		self.currentBMI = 0

		self.imgBanner = PhotoImage(file="images/Title.gif")
		self.banner = Label(self.application, height=106, image=self.imgBanner)

		self.footer = Label(self.application, text="version 1.0 | 01/10/2020 - ", font=self.smallFont)
		self.footer['bg'] = "#E3FBFA"
		self.footer['fg'] = "#3366FF"

		self.webURL = Label(self.application, text="Seb2lyon", font=self.smallLinkFont, cursor="hand2")
		self.webURL['bg'] = "#E3FBFA"
		self.webURL['fg'] = "#3366FF"
		self.webURL.bind("<Button-1>", lambda e: self.goToUrl("http://seb2lyon.info.free.fr"))

		self.banner.place(x=0, y=0)
		self.footer.place(x=126, y=471)
		self.webURL.place(x=310, y=471)

		self.welcome = welcomeWindow(self)


	def goToUrl(self, url):
		""" Function that permit to open a web browser
		in order to open my web site home page """
		webbrowser.open_new(url)

	def changeMainToSummary(self):
		""" Function that permit to jump from
		Welcome window
		to
		Summary window """ 	
		self.delWelcomeWindow()
		self.summary = summaryWindow(self)

	def changeMainToCreateAccountOne(self):
		""" Function that permit to jump from
		Main page
		to
		Creating account (page 1/2)""" 		
		self.delWelcomeWindow()
		self.createAccountOne = createAccountWindowOne(self)

	def changeCreateAccountOneToCreateAccountTwo(self):
		""" Function that permit to jump from
		Creating account (page 1/2)
		to
		Creating account (page 2/2) """ 		
		self.delCreateAccountWindowOne()
		self.createAccountTwo = createAccountWindowTwo(self)

	def changeCreateAccountTwoToCreateAccountOne(self):
		""" Function that permit to jump from
		Creating account (page 2/2)
		to
		Creating account (page 1/2) """ 		
		self.delCreateAccountWindowTwo()
		self.createAccountOne = createAccountWindowOne(self)

	def changeCreateAccountOneToMain(self):
		""" Function that permit to jump from
		Creating account (page 1/2)
		to
		Main window """
		self.delCreateAccountWindowOne()

		del self.currentUser
		self.currentUser = userClass()

		self.welcome = welcomeWindow(self) 	

	def changeCreateAccountTwoToSummary(self):
		""" Function that permit to jump from
		Creating account (page 2/2)
		to
		Summary window """ 	
		self.delCreateAccountWindowTwo()
		self.summary = summaryWindow(self)

	def changeSummaryToCreateAccountOne(self):
		""" Function that permit to jump from
		Summary
		to
		Creating account (page 1/2) """ 
		self.delSummaryWindow()
		self.createAccountOne = createAccountWindowOne(self)	

	def changeCreateAccountOneToSummary(self):
		""" Function that permit to jump from
		Creating account (page 1/2)
		to
		Summary """ 
		self.delCreateAccountWindowOne()

		file = open("config/users", "rb")

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
		i = 0

		while i < nbrUsers:
			if appUsers[i].userPseudo == self.currentUser.userPseudo:
				del self.currentUser
				self.currentUser = appUsers[i]
			i = i + 1

		self.summary = summaryWindow(self)

	def changeSummaryToMain(self):
		""" Function that permit to jump from
		Summary
		to
		Main window """ 

		self.delSummaryWindow()
		del self.currentUser
		self.currentUser = userClass()
		self.welcome = welcomeWindow(self)

	def changeSummaryToHeightAndWeight(self):
		""" Function that permit to jump from
		Summary
		to
		Height and Weight window """ 
		self.delSummaryWindow()
		self.heightAndWeight = heightAndWeightWindow(self) 

	def changeHeightAndWeightToResults(self):
		""" Function that permit to jump from
		Height and Weight window
		to
		the Results page """
		self.delHeightAndWeightWindow()
		self.results = resultsWindow(self)

	def createHistoryWindow(self):
		""" Function that permit to create the History Window """
		self.history = historyWindow(self)

	def delWelcomeWindow(self):
		""" Destroy Welcome window """
		self.welcome.subTitle.destroy()
		self.welcome.labelConnect.destroy()
		self.welcome.labelID.destroy()
		self.welcome.entryID.destroy()
		self.welcome.labelPass.destroy()
		self.welcome.entryPass.destroy()
		self.welcome.buttonConnect.destroy()
		self.welcome.labelWarningConnexion.destroy()
		self.welcome.labelNoAccount.destroy()
		self.welcome.labelCreateAccount.destroy()
		del self.welcome

	def delCreateAccountWindowOne(self):
		""" Destroy Create account window (part 1/2) """
		self.createAccountOne.labelFirstName.destroy()
		self.createAccountOne.entryFirstName.destroy()
		self.createAccountOne.labelGender.destroy()
		for i in range(2):
			self.createAccountOne.radioStock[i].destroy()
		self.createAccountOne.radioGender.destroy()
		self.createAccountOne.labelBirthDate.destroy()
		self.createAccountOne.entryBirthDay.destroy()
		self.createAccountOne.entryBirthMonth.destroy()
		self.createAccountOne.entryBirthYear.destroy()
		self.createAccountOne.labelSlash1.destroy()
		self.createAccountOne.labelSlash2.destroy()
		self.createAccountOne.labelWarningConnexion.destroy()
		self.createAccountOne.buttonCancel.destroy()
		self.createAccountOne.buttonNext.destroy()
		del self.createAccountOne

	def delCreateAccountWindowTwo(self):
		""" Destroy Create account window (part 2/2) """
		self.createAccountTwo.labelPseudo.destroy()
		self.createAccountTwo.entryPseudo.destroy()
		self.createAccountTwo.labelPasswd1.destroy()
		self.createAccountTwo.entryPasswd1.destroy()
		self.createAccountTwo.labelPasswd2.destroy()
		self.createAccountTwo.entryPasswd2.destroy()
		self.createAccountTwo.labelWarningConnexion.destroy()
		self.createAccountTwo.buttonPrevious.destroy()
		self.createAccountTwo.buttonValidate.destroy()
		del self.createAccountTwo

	def delSummaryWindow(self):
		""" Destroy Summary window """
		self.summary.labelCheck1.destroy()
		self.summary.labelCheck2.destroy()
		self.summary.labelCheck3.destroy()
		self.summary.labelFirstName1.destroy()
		self.summary.labelFirstName2.destroy()
		self.summary.labelGender1.destroy()
		self.summary.labelGender2.destroy()
		self.summary.labelBirthDate1.destroy()
		self.summary.labelBirthDate2.destroy()
		self.summary.buttonModify.destroy()
		self.summary.buttonConfirm.destroy()
		self.summary.labelDeleteAccount.destroy()
		del self.summary

	def delHeightAndWeightWindow(self):
		""" Destroy Height and Weight window """
		self.heightAndWeight.labelHeight.destroy()
		self.heightAndWeight.entryHeight.destroy()
		self.heightAndWeight.labelCentimeters.destroy()
		self.heightAndWeight.labelWeight.destroy()
		self.heightAndWeight.entryWeight.destroy()
		self.heightAndWeight.labelKilograms.destroy()
		self.heightAndWeight.labelWarningConnexion.destroy()
		self.heightAndWeight.buttonCalculate.destroy()
		del self.heightAndWeight
