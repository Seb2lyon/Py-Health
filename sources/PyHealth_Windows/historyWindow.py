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

		self.myCanvas = Canvas(self, bg='#E3FBFA', height=400, width=700)		
		self.myCanvas.create_image(15, 15, anchor=NW, image=self.imageGrid)

		self.myCanvas.place(x=0, y=0)
