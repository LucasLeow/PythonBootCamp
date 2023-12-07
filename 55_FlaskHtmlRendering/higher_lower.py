from flask import Flask
import random

app = Flask(__name__)
ans = random.randint(0, 9)
@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="gif showing numbers from 0 to '
            '9"/>')

@app.route('/<int:num>')
def check_num(num):
    if num < ans:
        return ('<h1 style="color: red;"/> Too low, try again! </h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>')
    elif num > ans:
        return ('<h1 style="color: purple;"/> Too high, try again! </h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>')
    else:
        return ('<h1 style="color: green;"/>You found me! </h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>')

if __name__ == '__main__':
    print(ans)
    app.run(debug=True)