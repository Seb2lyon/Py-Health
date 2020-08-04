import webbrowser
from PyHealth_Windows.welcomeWindow import *
from PyHealth_Windows.createAccountWindowOne import *

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
		self.application['bg'] = "#E4E4E4"

		self.smallFont = Font(family="Arial Black", size=10)
		self.smallLinkFont = Font(family="Arial Black", size=10, underline=1)
		self.normalFont = Font(family="Arial Black", size=11)
		self.normalItalicFont = Font(family="Arial Black", size=11, slant="italic")
		self.normalLinkFont = Font(family="Arial Black", size=11, underline=1)
		self.normalInputFont = Font(family="Arial", size=11)
		self.largeFont = Font(family="Arial Black", size=12)

		self.imgBanner = PhotoImage(file="images/Titre.gif")
		self.banner = Label(self.application, height=106, image=self.imgBanner)

		self.footer = Label(self.application, text="version 1.0 | 03/08/2020 - ", font=self.smallFont)
		self.footer['bg'] = "#E4E4E4"
		self.footer['fg'] = "#008000"

		self.webURL = Label(self.application, text="Seb2lyon", font=self.smallLinkFont, cursor="hand2")
		self.webURL['bg'] = "#E4E4E4"
		self.webURL['fg'] = "#008000"
		self.webURL.bind("<Button-1>", lambda e: self.goToUrl("http://seb2lyon.info.free.fr"))

		self.banner.place(x=0, y=0)
		self.footer.place(x=126, y=471)
		self.webURL.place(x=310, y=471)

		self.welcome = welcomeWindow(self)

	def goToUrl(self, url):
			webbrowser.open_new(url)

	def changeMainToCreateAccountOne(self):
		""" Function that permit to jump from
		Main page
		et
		Creating account (page 1/2)""" 		
		self.welcome.subTitle.destroy()
		self.welcome.labelConnect.destroy()
		self.welcome.labelID.destroy()
		self.welcome.entryID.destroy()
		self.welcome.labelPass.destroy()
		self.welcome.entryPass.destroy()
		self.welcome.buttonConnect.destroy()
		# page.warningConnexion.destroy()
		self.welcome.labelNoAccount.destroy()
		self.welcome.labelCreateAccount.destroy()
		del self.welcome

		self.createAccountOne = createAccountWindowOne(self)
