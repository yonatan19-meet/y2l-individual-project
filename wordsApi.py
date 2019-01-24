import requests
import json
import random

def definitionOfWord(word):
	response = requests.get("https://dictionaryapi.com/api/v3/references/learners/json/" + word + "?key=3e440dde-7584-4967-af7a-4e9d40c9df87")
	parsed_content = json.loads(response.content)
	if parsed_content == []:
		return False
	elif type(parsed_content[0]) is unicode:
		return False
	else:
		length = len(parsed_content[0][u"meta"][u'app-shortdef'][u"def"])
		# print (length)
		if length == 1:
			return parsed_content[0][u"meta"][u'app-shortdef'][u"def"]
		else:
			index = random.randint(-1, length-1)
			return parsed_content[0][u"meta"][u'app-shortdef'][u"def"][index]

def find_a_word(word_requirements):
	response = requests.get("https://api.datamuse.com/words?sp=" + str(word_requirements))
	parsed_content = json.loads(response.content)
	length = len(parsed_content)
	index = random.randint(-1, length-1)
	# print(parsed_content)
	most_common_word = parsed_content[index][u'word']
	# words = parsed_content["word"]
	if definitionOfWord(str(most_common_word)) == False:
		most_common_word = find_a_word(word_requirements)[0]
		print(most_common_word)[0]
	definition = definitionOfWord(str(most_common_word))
	# print(definition)
	return [most_common_word, definition]

# print(definitionOfWord("datum"))

# word_requirements = "???????"
# print(find_a_word(word_requirements))
