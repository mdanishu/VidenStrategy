import mysql.connector
import config
import pandas as pd
import StockPull
import sqlalchemy
from sqlalchemy import create_engine
import pymysql

host = "JeaDanish"
user = "Danish"
passwd = config.pwd1
database = "stocks"

engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{database}", echo=True, future=True)
# engine = create_engine(f"mysql+mysqldb://usrid:password@localhost/my_db", echo=True, future=True)
# engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{database}", echo=True, future=True)

Tbl = "tickers"
SQLsel = f"SELECT * FROM {Tbl}"
# SQLDesc = f"Describe {Tbl}"

with engine.connect() as conn:
    # result = conn.execute(SQLsel)
    result = conn.execute(text("SELECT * FROM tickers"))
    print (result.all())
