class userClass:
	""" User attributes :
	- First name
	- Gender
	- Day of birth
	- Month of birth
	- Year of birth
	- Pseudo
	- Password (hashed) """

	def __init__(self):

		self.userExist = False
		self.userFirstName = ""
		self.userGender = "F"
		self.userDayOfBirth = ""
		self.userMonthOfBirth = ""
		self.userYearOfBirth = ""
		self.userPseudo = ""
		self.userPasswd = ""
		# HASH THE PASSWORD

		self.userHeight = ""
		self.userWeight = ""
		self.userBMI = [] 
		self.lastVisits = [] 

		#TODO : Hash the password
		
