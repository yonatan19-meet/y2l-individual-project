from flask import Flask, render_template, request
from model import blanks_list, size, typed_letters_dict, def_list
# from wordsApi import definitionOfWord
app = Flask(__name__)

@app.route('/')
def crossword():
		return render_template('crosswordTemplate.html', blanks_list = blanks_list, size = size, def_list = def_list)


@app.route('/check', methods = ['GET', 'POST'])
def check():
	if request.method == 'GET':
		return render_template('crosswordTemplate.html', blanks_list = blanks_list, size = size)
	elif request.method == 'POST':
		return render_template('checked_cross_temp.html', blanks_list = blanks_list, size = size, typed_letters_dict = typed_letters_dict)


if __name__ == '__main__':
    app.run(debug=True)

