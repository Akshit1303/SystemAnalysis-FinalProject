import sqlite3 as sql

conn = sql.connect("products.db")

conn.execute("CREATE TABLE products (Product Name TEXT, Description TEXT, Quantity TEXT, Checkin Date DATE)")

conn.close()

print("Table created successfully")