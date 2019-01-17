from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Square(Base):
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
			for i in range(length(word)):
				query_by_serial_number(first_letter_location+i)
				square.letter = letters_list[i]
	def generate_vertical_words(first_letter_location, word, blanks_list):
		letters_list = list(word)
			for i in range(length(word)):
				query_by_serial_number(first_letter_location+8*i)
				square.letter = letters_list[i]
	def create_template(new_blank_list):
		




def query_by_serial_number(serial_number):
	for square in squares:
		if square.column == first_letter_location%8 & square.row == first_letter_location/8:
			return square




