import psycopg2


class DBManager:
    def __init__(self, host="127.0.0.1", database="testDB", user="postgres", password="12345678", port="5434") -> None:
        print("DBManager created...")
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        print(self.host)
        self.conn = psycopg2.connect(
            host=self.host, database=self.database, user=self.user, password=self.password, port=self.port)

        self.cur = self.conn.cursor()

    def get_users(self):
        rows = None
        try:
            self.cur.execute(
                "SELECT * FROM usertable ORDER BY userid")
            rows = self.cur.fetchall()
        except Exception as e:
            print("get_users ERROR: " + str(e))
            rows = None
        return rows
