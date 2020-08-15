from tkinter import *
import datetime

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

		self.myCanvas = Canvas(self, bg='#E3FBFA', height=400, width=700, closeenough=0)
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

		self.historyCount = len(self.mainPage.currentUser.lastVisits)
		i = 0
		x = 15 + 33
		r = 5

		while i < self.historyCount:
			historyDate = datetime.date.fromtimestamp(self.mainPage.currentUser.lastVisits[i]).strftime('%d/%m/%Y')
			self.labelDates[i]['text'] = historyDate
			y = self.mainPage.currentUser.coordinatePoints[i] + 14
			self.myCanvas.create_oval(x-r, y-r, x+r, y+r, fill='black')

			x = x + 67
			i = i + 1	

		i = 0
		x = 15 + 33
		r = 5	

		while i < self.historyCount:
			if i > 0:
				self.myCanvas.create_line(x - 67, self.mainPage.currentUser.coordinatePoints[i-1] + 14, x, self.mainPage.currentUser.coordinatePoints[i] + 14, width=2)

			x = x + 67
			i = i + 1	

		if self.historyCount > 0:
			self.myCanvas.tag_bind(2, '<Enter>', lambda e: self.showToolTip(0))
			self.myCanvas.tag_bind(2, '<Leave>', self.deleteToolTip)
		if self.historyCount > 1:
			self.myCanvas.tag_bind(3, '<Enter>', lambda e: self.showToolTip(1))
			self.myCanvas.tag_bind(3, '<Leave>', self.deleteToolTip)
		if self.historyCount > 2:
			self.myCanvas.tag_bind(4, '<Enter>', lambda e: self.showToolTip(2))
			self.myCanvas.tag_bind(4, '<Leave>', self.deleteToolTip)
		if self.historyCount > 3:
			self.myCanvas.tag_bind(5, '<Enter>', lambda e: self.showToolTip(3))
			self.myCanvas.tag_bind(5, '<Leave>', self.deleteToolTip)
		if self.historyCount > 4:
			self.myCanvas.tag_bind(6, '<Enter>', lambda e: self.showToolTip(4))
			self.myCanvas.tag_bind(6, '<Leave>', self.deleteToolTip)
		if self.historyCount > 5:
			self.myCanvas.tag_bind(7, '<Enter>', lambda e: self.showToolTip(5))
			self.myCanvas.tag_bind(7, '<Leave>', self.deleteToolTip)
		if self.historyCount > 6:
			self.myCanvas.tag_bind(8, '<Enter>', lambda e: self.showToolTip(6))
			self.myCanvas.tag_bind(8, '<Leave>', self.deleteToolTip)
		if self.historyCount > 7:
			self.myCanvas.tag_bind(9, '<Enter>', lambda e: self.showToolTip(7))
			self.myCanvas.tag_bind(9, '<Leave>', self.deleteToolTip)
		if self.historyCount > 8:
			self.myCanvas.tag_bind(10, '<Enter>', lambda e: self.showToolTip(8))
			self.myCanvas.tag_bind(10, '<Leave>', self.deleteToolTip)
		if self.historyCount > 9:
			self.myCanvas.tag_bind(11, '<Enter>', lambda e: self.showToolTip(9))
			self.myCanvas.tag_bind(11, '<Leave>', self.deleteToolTip)			
	
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

	def showToolTip(self, rangeBMI):
		""" Show Tooltip with the BMI """
		self.labelToolTip = Label(self, bg='white', text=round(self.mainPage.currentUser.userBMI[rangeBMI], 2), font=self.mainPage.gridNormalFont)
		xToolTip = 48 + (67 * rangeBMI)
		yToolTip = self.mainPage.currentUser.coordinatePoints[rangeBMI] + 35
		self.labelToolTip.place(x=xToolTip, y=yToolTip)
		
	def deleteToolTip(self, event):
		""" Delete the tooltip """
		self.labelToolTip.destroy()

	def closeWindow(self):
		""" Close the History Window """
		self.destroy()
