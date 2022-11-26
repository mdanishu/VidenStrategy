import psycopg
import datetime


# hostname = 'localhost'
# database = 'postgres'
# username = 'postgres'
# pwd = 'donutking'
# port_id = 5432
numV1 = 1992

query1 = """CREATE TABLE stocklist (
            id serial PRIMARY KEY,
            ticker text)"""
queryDel = "DELETE FROM test WHERE num = 12"
queryIns = 0
querySel = 'SELECT * FROM TEST'
queryUp = "UPDATE test SET id = 1;"

with psycopg.connect("dbname=postgres user=postgres password=donutking") as conn:
    with conn.cursor() as cur:
        cur.execute(queryDel)
        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
                    (1, 'arkk'))
        i = 0
        for i in range(10):
            cur.execute(queryUp)
        cur.execute(querySel)
        # cur.execute(ALTER SEQUENCE 'id' RESTART WITH 0)

        for record in cur.fetchall():
            print(record[0], record[1], record[2])

        #      for i in range(3):
        #          print(record[1])
        #          i = i+1


cur.close()
conn.close()