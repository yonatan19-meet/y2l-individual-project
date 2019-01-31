import requests
import json
import random
global def_list
def_list = []

def definitionOfWord(word):
	response = requests.get("https://dictionaryapi.com/api/v3/references/learners/json/" + word + "?key=3e440dde-7584-4967-af7a-4e9d40c9df87")
	parsed_content = json.loads(response.content)
	try:
		if parsed_content == []:
			print("here")
			return False
		elif type(parsed_content[0]) is not dict:
			print("there")
			return False
		elif type(parsed_content[0][u"meta"][u'app-shortdef'][u"def"]) is list:
			# print(parsed_content[0][u"meta"][u'app-shortdef'][u"def"])
			length = len(parsed_content[0][u"meta"][u'app-shortdef'][u"def"])
			# print (length)
			if length == 1:
				return parsed_content[0][u"meta"][u'app-shortdef'][u"def"]
			else:
				index = random.randint(-1, length-1)
				return parsed_content[0][u"meta"][u'app-shortdef'][u"def"][index]
	except: 
		return False
		
def find_a_word(word_requirements):
	response = requests.get("https://api.datamuse.com/words?sp=" + str(word_requirements))
	parsed_content = json.loads(response.content)
	length = len(parsed_content)
	index = random.randint(-1, length-1) 
	# print(parsed_content)
	most_common_word = parsed_content[index][u'word']
	print(most_common_word)
	# words = parsed_content["word"]
	try:
		if most_common_word is not str:
			word_index = 0
			while definitionOfWord(str(most_common_word)) == False and word_index <= 1:
				print(definitionOfWord(str(most_common_word)))
				response = requests.get("https://api.datamuse.com/words?sp=" + str(word_requirements))
				parsed_content = json.loads(response.content)
				most_common_word = parsed_content[0][u'word']
				word_index += 1
				print(word_index)
			if definitionOfWord(str(most_common_word)) == False:
				return False
			else:
				definition = definitionOfWord(str(most_common_word))
		# print(definition)
				return [most_common_word, definition]
		else:
			definition = definitionOfWord(str(most_common_word))
		# print(definition)
			return [most_common_word, definition]		
	except:
		return False
