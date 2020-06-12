import db as db
from flask import Flask, render_template,request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     """Print 'Hello, World' as the response body."""
#     return 'Hello, World'

@app.route('/')
def employee_details():
    return render_template('h_page.html')

@app.route('/action_page', methods=['GET','POST'])
def action():
        data = request.form
        name = data['name']
        age = data['age']
        phone = data['phone']
        email = data['email']
        salary = data['sal']
        db.get_all_details(name,age,phone,email,salary)
        return "Added to db"

@app.route('/bye')
def bye_world():
    """Print 'Bye, World' as the response body."""
    return '<h1>Bye, World!</h1><br><h2>Welcome</h2>'
if __name__ == '__main__':
    app.run()