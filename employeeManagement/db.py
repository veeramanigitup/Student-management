import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employee(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

        #fetch all data form DB

    #Insert Function
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employee values (NULL,?,?,?,?,?,?,?)",(name,age,doj,email,gender,contact,address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT  * from employee")
        rows = self.cur.fetchall()
        return rows

    #delete record
    def remove(self,id):
        self.cur.execute("delete from employee where  id=?",(id,))
        self.con.commit()

    #Update Record
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employee set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?", (name, age, doj, email, gender, contact, address,id))
        self.con.commit()

#o=Database("Employee.db")
#o.insert("veera","21","03-08-2003","v3803@gmail.com","Male","6384","chennai")
#o.remove("1")
#o.update("2","vm","23","12-009-2000","racer@gmail.com","Male","638489","test")
#o.fetch()
