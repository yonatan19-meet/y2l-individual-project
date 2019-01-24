from flask import Flask, render_template
from model import *
app = Flask(__name__)

@app.route('/')
def crossword():
    return render_template('crosswordTemplate.html', blanks_list)

if __name__ == '__main__':
    app.run(debug=True)

