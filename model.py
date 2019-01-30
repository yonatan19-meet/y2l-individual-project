from __future__ import print_function
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from wordsApi import find_a_word
Base = declarative_base()
from array import *
from wordsApi import def_list

# engine = create_engine('sqlite:///')
# Session = sessionmaker(bind = engine)
# session = Session()


# Write your classes here :
global squares, blanks_list, size, typed_letters_list, def_list, secondary_vertical_locations_list, secondary_horizontal_locations_list
def_list = list()
size = 5
squares = list()
blanks_list = []
typed_letters_list = []
class Square:
	def __init__(self, letter, blank, row, column):
		self.letter = letter
		self.row = row
		self.column = column
		self.blank = blank
		serial_number = 5*row + column
		if self.blank == True:
			blanks_list.append(serial_number)
		squares.append(self)

def query_by_serial_number(serial_number):
	if serial_number > (size**2 - 1):
		pass
	for square in squares:
		if square.column == serial_number%size and square.row == serial_number/size:
			# print(square.letter)
			return square

def generate_first_horizon_words(first_letter_location, word):
	letters_list = list(word)
	for i in range(len(word)):
		query_by_serial_number(first_letter_location+i).letter = letters_list[i]
	
def generate_horizontal_words(first_letter_location):
	first_letter_location = first_letter_location
	sequence = ""
	a = True
	b = 0
	while a==True:
		if first_letter_location + b in blanks_list:
			a = False
			sequence = sequence
		elif query_by_serial_number(first_letter_location + b).letter == None:
			sequence += "?"
			b += 1
		else:
			sequence += str(query_by_serial_number(first_letter_location + b).letter)
			b += 1
	if find_a_word(sequence) == False:
		secondary_vertical(secondary_vertical_locations_list)
		secondary_horizontal(secondary_horizontal_locations_list)
		print("False")
	else:
		output = find_a_word(sequence)
		def_list.append(output[1])
		word = output[0]
		generate_first_horizon_words(first_letter_location, word)

def generate_first_vertical_words(first_letter_location, word):
	letters_list = list(word)
	for i in range(len(word)):
		query_by_serial_number(first_letter_location+size*i).letter = letters_list[i]

def generate_vertical_words(first_letter_location):
	first_letter_location = first_letter_location
	sequence = ""
	a = True
	b = 0
	while a==True and b<=(size**2 - 1):
		if (first_letter_location + b) in blanks_list:
			a = False
			sequence = sequence
		elif query_by_serial_number(first_letter_location + b).letter == None:
			# print(squares[first_letter_location+b].letter)
			sequence += "?"
			# print(sequence)
			b+=size
		else:
			sequence += str(query_by_serial_number(first_letter_location + b).letter)
			b += size
	result = find_a_word(sequence)
	if result == False:
		secondary_vertical(secondary_vertical_locations_list)
		secondary_horizontal_locations_list(secondary_horizontal_locations_list)
		print("False")
	else:
		def_list.append(result[1])
		word = result[0]
		generate_first_vertical_words(first_letter_location, word)
		
def create_template(new_blank_list):
	for blank in new_blank_list:
		query_by_serial_number(blank).blank = True
		blanks_list.append(query_by_serial_number(blank))
	print(blanks_list)

def make_a_template():
	for i in range(size):
		for box in range(size):
			box = Square(None, False, i, box)
			# print("I am here")

def generate_blanks_list(blanks_list):
	for i in blanks_list:
		query_by_serial_number(i).blank = True
		# print("I am here")
	return blanks_list

make_a_template()

blanks_list = [0, 24, 4, 20, 12, 2, 22, 10, 14]

generate_blanks_list(blanks_list)

def initial(initial_words_list, initial_locations_list):
	for i in range(len(initial_words_list)):
		a = initial_locations_list[i]
		b = initial_words_list[i]
		# print(b)
		generate_first_horizon_words(a, b)

initial_words_list = []
initial_locations_list = []
# initial(initial_words_list, initial_locations_list)

def secondary_vertical(secondary_vertical_locations_list):
	for position in secondary_vertical_locations_list:
		generate_vertical_words(position)

def secondary_horizontal(secondary_horizontal_locations_list):
	for position in secondary_horizontal_locations_list:
		generate_horizontal_words(position)
	view_the_crossword()

secondary_vertical_locations_list = [1, 3]
secondary_horizontal_locations_list = [5, 15]


def view_the_crossword():
	letters = []
	a = list()
	print("we got here")
	for c in range(size):
		a = []
		for i in range(size):
			a.append(query_by_serial_number(c*size+i).letter)
		letters.append(a)
	for line in letters:
		for letter in line:
			print(str(letter)+" ", end='')
		print()
	return(letters)

# session.add(total)
# session.commit()


