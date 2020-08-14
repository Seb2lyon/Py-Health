from tkinter import *

class historyWindow(Toplevel):
	""" Pop-up window that display the history of the user BMI :
	 - graph with dates and BMI levels
	 - BMI number is displayed in a tooltip """

	def __init__(self, page):
		Toplevel.__init__(self, page)

		self.mainPage = page

		self.grab_set()
		self.transient(self.mainPage)
		self.geometry("700x400")
		self.resizable(False, False)
		self['bg'] = '#E3FBFA'
		self.title("Py Health - Votre historique")

		self.imageGrid = PhotoImage(file="images/Grid.gif")
		self.imageBlueLabel = PhotoImage(file="images/BlueLabel.gif")
		self.imageGreenLabel = PhotoImage(file="images/GreenLabel.gif")
		self.imageRedLabel = PhotoImage(file="images/RedLabel.gif")
		self.imageOrangeLabel = PhotoImage(file="images/OrangeLabel.gif")

		self.myCanvas = Canvas(self, bg='#E3FBFA', height=400, width=700)
		self.myCanvas.create_image(15, 15, anchor=NW, image=self.imageGrid)

		self.labelDates = []

		self.labelDate1 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate1)
		self.labelDate2 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate2)
		self.labelDate3 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate3)
		self.labelDate4 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate4)
		self.labelDate5 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate5)
		self.labelDate6 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate6)
		self.labelDate7 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate7)
		self.labelDate8 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate8)
		self.labelDate9 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)
		self.labelDates.append(self.labelDate9)
		self.labelDate10 = Label(self, bg='#E3FBFA', height=1, width=10, font=self.mainPage.gridNormalFont)	
		self.labelDates.append(self.labelDate10)

		self.myCanvas.create_image(15, 288, anchor=NW, image=self.imageRedLabel)
		self.myCanvas.create_image(15, 312, anchor=NW, image=self.imageOrangeLabel)
		self.myCanvas.create_image(15, 336, anchor=NW, image=self.imageGreenLabel)
		self.myCanvas.create_image(15, 360, anchor=NW, image=self.imageBlueLabel)

		self.myCanvas.create_text(41, 289, anchor=NW, text="Obésité", font=self.mainPage.gridBoldFont)
		self.myCanvas.create_text(41, 313, anchor=NW, text="Surpoids", font=self.mainPage.gridBoldFont)
		self.myCanvas.create_text(41, 337, anchor=NW, text="Corpulence normale", font=self.mainPage.gridBoldFont)
		self.myCanvas.create_text(41, 361, anchor=NW, text="Dénutrition", font=self.mainPage.gridBoldFont)

		self.buttonClose = Button(self, text="Fermer", font=self.mainPage.normalFont, width=10, command=self.closeWindow)
		self.buttonClose['bg'] = "#969696"
		self.buttonClose['fg'] = "#FFFFFF"

		self.myCanvas.place(x=0, y=0)
		self.labelDate1.place(x=15, y=255)
		self.labelDate2.place(x=82, y=255)
		self.labelDate3.place(x=149, y=255)
		self.labelDate4.place(x=216, y=255)
		self.labelDate5.place(x=283, y=255)
		self.labelDate6.place(x=350, y=255)
		self.labelDate7.place(x=417, y=255)
		self.labelDate8.place(x=484, y=255)
		self.labelDate9.place(x=551, y=255)
		self.labelDate10.place(x=618, y=255)
		self.buttonClose.place(x=550, y=330)

	def closeWindow(self):
		""" Close the History Window """
		self.destroy()

		# INFO : Point size = 10
