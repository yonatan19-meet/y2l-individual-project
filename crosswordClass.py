from model import *
from database import session

class Square:
	def __init__(self, letter, blank, row, column):
		self.letter = letter
		self.row = row
		self.column = column
		serial_number = 8*row + column
		blanks_list = []
		if self.blank == True:
			blanks_list.append(serial_number)
		squares = []
		squares.append(self)
	def generate_horizon_words(first_letter_location, word, blanks_list):
		letters_list = list(word)
		for square in squares:
			if square.column == first_letter_location%8 & square.row == first_letter_location/8:
				square.letter = letters_list[0]
				for i in range (length(word)-1):

Square(a, False, 2, 1)
a = session.query_by(row = 2)
print(a.letter)

