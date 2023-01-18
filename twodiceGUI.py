"""
1/10/2023 Program: twodiceGUI.py

GUI-based version of the two dice application. random numbers are generated and compared

NOTE: the file breezypythongui.py must be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random
# other imports can go here

class TwoDiceGUI(EasyFrame):

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Two Dice Game", width = 340, height = 280, resizable = False, background = "SeaGreen")
		self.addLabel(text = "Two Dice Game", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "SeaGreen", foreground = "white", font = Font(family = "Impact", size = 26))
		# PLAYER
		self.addLabel(text = "Player's Roll:", row = 1, column = 0, background = "SeaGreen")
		self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, width = 4, state = "readonly")
		# COMPUTER
		self.addLabel(text = "Computer's Roll:", row = 2, column = 0, background = "SeaGreen")
		self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 1, width = 4, state = "readonly")
		# BUTTON / RESULTS
		self.addButton(text = "Roll the Dice!", row = 3, column = 0, columnspan = 2, command = self.roll)
		self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 2, sticky = "NSEW", background = "SeaGreen", foreground = "white", font = Font(family = "Georgia", size = 22))

	# definition of the self.roll() function which handles the event
	def roll(self):
		# variables for the function
		die1 = random.randint(1, 6)
		die2 = random.randint(1, 6)

		# processing phase
		if die1 > die2:
			result = "You win!!"
			self.resultArea["foreground"] = "yellow"
		elif die1 < die2:
			result = "You lose!"
			self.resultArea["foreground"] = "red"
		else:
			result = "It's a draw!"
			self.resultArea["foreground"] = "white"

		# output phase
		self.playerRoll.setNumber(die1)
		self.computerRoll.setNumber(die2)
		self.resultArea["text"] = result

# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	TwoDiceGUI().mainloop()

# global call to the main() method
main()