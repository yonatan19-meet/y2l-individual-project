from flask import Flask, render_template, request
from time import sleep
from model import blanks_list, size, typed_letters_list, def_list, secondary_vertical_locations_list, view_the_crossword, secondary_horizontal_locations_list, secondary_vertical, secondary_horizontal
# from wordsApi import definitionOfWord
app = Flask(__name__, static_folder = 'y2l-individual-project/static')

@app.route('/', methods = ['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/home', methods = ['GET', 'POST'])
def crossword():
	if request.method == 'POST':
		secondary_vertical(secondary_vertical_locations_list)
		sleep(2)
		secondary_horizontal(secondary_horizontal_locations_list)
		return render_template('crosswordTemplate.html', blanks_list = blanks_list, size = size, def_list = def_list, secondary_vertical_locations_list = secondary_vertical_locations_list, secondary_horizontal_locations_list = secondary_horizontal_locations_list)
	else:
		return render_template('home.html')


@app.route('/check', methods = ['GET', 'POST'])
def check():
	if request.method == 'GET':
		return render_template('crosswordTemplate.html', blanks_list = blanks_list, size = size, def_list = def_list, secondary_vertical_locations_list = secondary_vertical_locations_list, secondary_horizontal_locations_list = secondary_horizontal_locations_list)
	elif request.method == 'POST':
		typed_letters_list = []
		for i in range(size):
			b  = []
			for q in range(size):
				index = size*i + q
				index = str(index)
				a = request.form.get(index, False)
				b.append(a)
			typed_letters_list.append(b)
		print(typed_letters_list)
		view = view_the_crossword()
		print(view)
		if typed_letters_list == view_the_crossword():
			return render_template('youWon.html')
		else:
			return render_template('crosswordTemplate.html', blanks_list = blanks_list, size = size, def_list = def_list)

if __name__ == '__main__':
    app.run(debug=True)

