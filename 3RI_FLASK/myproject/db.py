import sqlite3 as lite
import sys
def get_all_details(name,age,phone,email,salary):
    try:
        con = lite.connect('C:\\Users\\Mahobiya_Mension\\WEB\\databse_1.bd')
        # cur = con.cursor()
        # cur.execute('SELECT SQLITE_VERSION()')
        # data = cur.fetchone()
        # print ("SQLite version: %s" % data)
        with con:
            cur = con.cursor()
            try:
                cur.execute("CREATE TABLE Basic(Id TEXT, Name TEXT, AGE INT)")
                cur.execute("CREATE TABLE Contact(Id TEXT, Phone INT, Email TEXT)")
                cur.execute("CREATE TABLE Salary(Id TEXT, Salary INT)")
            except:
                pass
            finally:
                print ("Enter your Basic details -- ")
                quit = "NO"
                if quit == 'y':
                    get_all_details(cur)
                    sys.exit(1)
                elif quit == 'delall':
                    cur.execute("DELETE FROM Basic")
                    cur.execute("DELETE FROM Contact")
                    cur.execute("DELETE FROM Salary")
                    sys.exit(1)
                # name = input("Your Name: ")
                # age = int(input("Your age (in numbers): "))
                # phone = int(input("Your Phone number: "))
                # email = input("Your Email ID: ")
                # salary = input("Your Salary: ")
                name_split = name.split(" ")
                if len(name_split) < 3:
                    ID = ''.join(string[0] for string in name_split) + "0" + str(age)
                else:
                    ID = ''.join(string[0] for string in name_split) + str(age)
                basic_query = "INSERT INTO Basic VALUES('{}','{}', {})".format(ID, name, age)
                contact_query = "INSERT INTO Contact VALUES('{}','{}', '{}')".format(ID, phone, email)
                salary_query = "INSERT INTO Salary VALUES('{}',{})".format(ID, salary)
                print (basic_query)
                cur.execute(basic_query)
                cur.execute(contact_query)
                cur.execute(salary_query)
                con.commit()
        # cur.execute("SELECT Name, ID FROM Users")
        # rows = cur.fetchall()
        # for row in rows:
        #     print (row)
    except Exception as e:
        print ("Error %s:" % e)
        sys.exit(1)