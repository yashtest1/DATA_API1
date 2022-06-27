#!/usr/bin/python3
# -*- coding: utf-8 -*-

from psycopg2 import connect

table_name = "installation"
conn = connect(
    dbname = "awesomeinc",
    user = "interviewee",
    host = "172.28.1.4",
    password = "wannasucceed"
)
cursor = conn.cursor()
cursor.execute(f"select * from {table_name};")
for i, record in enumerate(cursor):
    print ("\n", type(record))
    print ( record )
cursor.close()
conn.close()
