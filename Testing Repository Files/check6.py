import mysql.connector
import requests
import pandas as pd

try:
    connection = mysql.connector.connect(host='githubproject.c8jutrmzxarx.ap-south-1.rds.amazonaws.com',
                                         database='githubinfo',
                                         port='3306',
                                         user='admin',
                                         passwd='github123')
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO githubtable VALUES ('company','1','1','[abc@m.com]','a/b','2021-02-15 to 2021-02-25','2021-02-25')" )
    # cur.execute("""SELECT * FROM githubtable""")
    # query_results = cur.fetchall()
    connection.commit()
except Exception as e:
    print("Database connection failed due to {}".format(e))