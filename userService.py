from db_manager import DBManager

db_manager = DBManager(host="127.0.0.1", database="testDB",
                       user="postgres", password="123456", port="5434")

rows = db_manager.get_users()

if rows:
    for row in rows:
        print(row)
