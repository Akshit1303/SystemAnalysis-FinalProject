from cProfile import run
from crypt import methods
import email
from email import message
from unicodedata import name
from flask import Flask, redirect, url_for, request, render_template 
import sqlite3 as sql

app = Flask(__name__)

@app.route("/<int:score>")
def hello_world(score):
    return render_template("home.htm", score=score)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        return redirect(url_for("success", name=username))

@app.route("/product")
def customer():
    return render_template("dataentry.htm")

@app.route("/addrec/", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        nm = request.form["nm"]
        desc = request.form["desc"]
        quan = request.form["quan"]
        date = request.form["date"]

    with sql.connect("products.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO products (Product Name, Description, Quantity, Checkin Date) VALUES ('{0}', '{1}', '{2}', '{3}')".format(nm, desc, quan, date))
        con.commit()
        message = "Product record added successfully"

    return render_template("summary.htm", msg = message)

@app.route("/list/")
def list():
    con = sql.connect("products.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()
    return render_template("list.htm", rows = rows)

if __name__ == "__main__":
    app.run()
