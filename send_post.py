import select

import psycopg2
import requests
import json

url = 'http://127.0.0.1:5000/db_data'

headers = {'Content-Type': 'application/json'}
myobj = {'somekey': 'somevalue'}

connection = psycopg2.connect(host="127.0.0.1",database="testDB",user="postgres",password="12345678",port="5434")
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur = connection.cursor()
cur.execute("LISTENING...")
while True:
    print("listening")
    select.select([connection],[],[])
    connection.poll()
    events = []
    while connection.notifies:
        notify = connection.notifies.pop().payload
        print ("Got NOTIFY:" ,notify)
        try:
            json_data = json.loads(notify)
            x = requests.post(url, json = json_data,verify=False,headers=headers)
            print(x)
        except Exception as msg:
            print("error: " + str(msg))


