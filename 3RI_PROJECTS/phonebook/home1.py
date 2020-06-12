import db_extract as db1
import db_add_contact as db2
import sqlite3 as lite
con= None
con = lite.connect('C:/Users/user/.spyder-py3/Python_programs/phonebook/database/Phonebook.db')
cur = con.cursor()

from flask import Flask, render_template,request,jsonify
app = Flask(__name__, template_folder='C://Users//user//.spyder-py3//Python_programs//phonebook//templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/p_search')
def p_search():
    return render_template('searchform.html')

@app.route('/p_add')
def p_add():
    return render_template('addcontact_form.html')

@app.route('/action_search', methods=['GET','POST'])
def action_search():
    if request.method == 'POST':
        data = request.form['search']
        cur.execute('SELECT fname,moblie from addcontact WHERE fname LIKE {}'.format(data))
        con.commit()
        data=cur.fetchall()
        return print(data)

@app.route('/action_add', methods=['GET','POST'])
def action_add():
        data = request.form
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        mobile = data['mobile']
        db2.get_all_det(fname,lname,email,mobile)
        return render_template('successfully_added.html')
if __name__ == '__main__':
    app.run()