import requests
import json

word_requirements = "cel????"
response = requests.get("https://api.datamuse.com/words?sp=" + word_requirements)

parsed_content = json.loads(response.content)
most_common_word = parsed_content[0][u'word']
# words = parsed_content["word"]
print(most_common_word)



