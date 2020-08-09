class userClass:
	""" User attributes :
	- First name
	- Gender
	- Day of birth
	- Month of birth
	- Year of birth
	- Pseudo
	- Password (hashed)
	- Height
	- Weight
	- Historic of BMI (results)
	- Historic of BMI (dates) """

	def __init__(self):

		self.userExist = False
		self.userFirstName = ""
		self.userGender = "F"
		self.userDayOfBirth = ""
		self.userMonthOfBirth = ""
		self.userYearOfBirth = ""
		self.userPseudo = ""
		self.userPasswd = ""
		self.userHeight = ""
		self.userWeight = ""
		self.userBMI = [] 
		self.lastVisits = [] 
