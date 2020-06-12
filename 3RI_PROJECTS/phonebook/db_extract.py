import sqlite3 as lite
from flask import Flask, render_template,request,jsonify
app = Flask(__name__, template_folder='C://Users//Mahobiya_Mension//Documents//phonebook//templates')
con = None
def get_all_contact(search):
    try:
        con = lite.connect('C:/Users/Mahobiya_Mension/Documents/phonebook/database/Phonebook.db')
        cur = con.cursor()
    except:
        pass
    finally:
        query_extract= ("select * from addcontact where fname='{}'".format(search))
        cur.execute(query_extract)
        con.commit()
        data = cur.fetchall()
        return data
