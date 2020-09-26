import sqlite3 as lite
con = None
try:
    con = lite.connect('aysi.db')
    cur = con.cursor()
    query = "CREATE  TABLE BASIC(Id TEXT,Name TEXT, Age INT)"
    cur.execute(query)
    
except lite.Error as e:
    pass
finally:
    name='pratik'
    Id='aq12'
    age=22
    query1="insert into BASIC values('{}','{}',{})".format(Id,name,age)
    cur.execute(query1)
    con.commit()
    if con:
        con.close()
