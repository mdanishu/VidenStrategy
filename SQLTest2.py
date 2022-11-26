import mysql.connector
import config
import pandas as pd
import StockPull
import sqlalchemy

db = mysql.connector.connect(
    host="JeaDanish",
    user="Danish",
    passwd=config.pwd1,
    database="stocks"
)

Tbl = "time1"
val = StockPull.analysisout('AAPL')
mycursor = db.cursor()
SQLsel = f"SELECT * FROM {Tbl}"
# SQLDesc = f"Describe {Tbl}"
# SQLins,
cols = "','".join([str(i) for i in val.columns.tolist()])

for i,row in val.iterrows():
    SQLins = "INSERT INTO time1 (`"+cols +"`) VALUES (" + "%s,"*(len(row)-1) + '%s)"
    mycursor.execute(SQLins, tuple(row))
    # mycursor.execute("INSERT INTO tickers (Date, Price, volume) VALUES (%s,%s,%s)", (val))

# db.commit()
mycursor.execute(SQLsel)

# print(val)
print(mycursor.fetchall())
print(mycursor.fetchwarnings())
print(type(mycursor.fetchall()))
# db.commit()
