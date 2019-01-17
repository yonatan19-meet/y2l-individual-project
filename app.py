from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def crossword():
    return render_template('crosswordTemplate.html')

if __name__ == '__main__':
    app.run(debug=True)

