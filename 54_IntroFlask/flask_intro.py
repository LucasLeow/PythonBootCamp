from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/username/<name>')
def greet(name):
    return f'Hello there {name}'

@app.route('/<name>/<int:number>') # converts number to int instead of string
def get_name_number(name, number):
    return f'Name: {name}, number: {number}'

if __name__=='__main__':
    app.run(debug=True) # debug mode, auto reload on change / access to flask debugger