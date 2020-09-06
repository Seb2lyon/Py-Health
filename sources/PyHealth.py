######################################
#             Py Health              #
#               v 1.0                #
#              --------              #
# Created and developped by Seb2lyon #
#      08-03-2020 to 10-01-2020      #
#              --------              #
#         Enjoy and Be safe!         #
#                                    #
######################################

# This program (in French) will calculate your BMI (Body Mass Index) in order to help you to evaluate your health condition.
# You can create an account (saved only on your local computer) in order to check periodically your BMI.
# This app is totally free and is able to calculate the BMI of every people aged from 1 year old.

from PyHealth_Windows.mainWindow import *

# Application script

app = Tk()

interface = mainWindow(app)

interface.mainloop()
