import db_extract as db1
import db_add_contact as db2

from flask import Flask, render_template,request,jsonify
app = Flask(__name__, template_folder='C://Users//Mahobiya_Mension//Documents//phonebook//templates')

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
    if request.method == "POST":
        data = request.form['search']
        dta=db1.get_all_contact(data)
    return render_template('view.html',data=dta)

 
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
    app.run(debug=True)