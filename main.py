from flask import Flask, render_template,url_for,redirect,request
from flask_mysqldb import MySQL

# import MySQLdb
# ,render_template,mysql py -3.9 -m pip install mysql-connector-python

app = Flask(__name__,template_folder='template')

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "anbesivam"
app.config["MYSQL_DB"] = "crud"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)


@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "select * from users"
    con.execute(sql)
    res = con.fetchall()
    return render_template("home.html",datas=res)

@app.route("/adduser",methods=['GET','POST'])
def adduser():
    if request.method=='POST':
        name=request.form['name']
        city = request.form['city']
        age = request.form['age']
        con=mysql.connection.cursor()
        sql="insert into users (NAME,CITY,AGE) value (%s,%s,%s)"
        con.execute(sql,[name,city,age])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("adduser.html")

#Update user
@app.route("/edituser/<string:id>",methods=['GET','POST'])
def edituser(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        sql = "update users set NAME=%s,CITY=%s,AGE=%s where ID=%s"
        con.execute(sql,[name,city,age,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for('home'))
        #con = mysql.connection.cursor()

    sql = "select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("edituser.html", datas=res)

#Delete user
@app.route("/deleteuser/<string:id>",methods=['GET','POST'])
def deleteuser(id):
    con = mysql.connection.cursor()
    sql = "delete from users where ID=%s"
    con.execute(sql, id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))

if (__name__ == '__main__'):
    app.run(debug=True)
    # con=mysql.connection.cursor
    # return render_template(home.html)





