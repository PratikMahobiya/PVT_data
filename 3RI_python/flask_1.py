from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world!'

@app.route('/bye')
def bye_world():
    return '<h1>bye, world!</h1><br><h2>sayyonara</h2><br><h3>welcome</h3>'

if __name__=='__main__':
    app.run(debug=True)