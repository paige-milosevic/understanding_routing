from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Paige Rocks'

@app.route('/dojo')
def print_dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def say(name):
    return f'Hello {name}'

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(num,phrase):
    output = ''
    for i in range(0,num):
        output += f'<p>{phrase}<p>'
    return output


if __name__=='__main__':
    app.run(debug=True)

