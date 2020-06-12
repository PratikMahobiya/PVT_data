import sqlite3 as lite
con = None
def get_all_det(fname,lname,email,mobile):
    try:
        con = lite.connect('C:/Users/Mahobiya_Mension/Documents/phonebook/database/Phonebook.db')
        cur = con.cursor()
        query_add = "CREATE  TABLE addcontact(fname varchar(20),lname varchar(20),email varchar(30),mobile int(10))"
        cur.execute(query_add)
    except:
        pass
    finally:
            query_ins= "INSERT INTO addcontact VALUES('{}','{}','{}',{})".format(fname,lname,email,mobile)
            cur.execute(query_ins)
            con.commit()
            con.close()
