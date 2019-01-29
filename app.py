from flask import Flask, render_template, request
from model import blanks_list, size, typed_letters_list, def_list, total
# from wordsApi import definitionOfWord
app = Flask(__name__)

@app.route('/')
def crossword():
		return render_template('crosswordTemplate.html', blanks_list = blanks_list, size = size, def_list = def_list)


@app.route('/check', methods = ['GET', 'POST'])
def check():
	if request.method == 'GET':
		return redirect(url_for('/'))
	elif request.method == 'POST':
		for i in range(size):
			for q in range(size):
				index = size*i + q
				index = str(index)
				a = request.form[index]
				typed_letters_list.append(a)
		if typed_letters_list == total:
			return render_template('youWon.html')
		else:
			return redirect(url_for('/'))

if __name__ == '__main__':
    app.run(debug=True)

