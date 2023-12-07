from flask import Flask

app = Flask(__name__)

# Text modification decorators

def bold(func):
    def make_bold():
        txt = func()
        bold_txt = '<b>' + txt + '</b>'
        return bold_txt

    return make_bold

def emphasis(func):
    def make_emphasis():
        txt = func()
        emphasis_txt = '<em>' + txt + '</em>'
        return emphasis_txt

    return make_emphasis

def underline(func):
    def make_underline():
        txt = func()
        return '<u>' + txt + '</u>'
    return make_underline

@app.route('/bye')
@bold
@emphasis
@underline
def bye():
    return 'Bye!'

if __name__ == '__main__':
    app.run(debug=True)