import os

import mysql.connector

dbconfig = {
    "host": os.getenv('PROXYSQL_HOST'),
    "port": os.getenv('PROXYSQL_PORT'),
    "user": os.getenv('PROXYSQL_USER'),
    "password": os.getenv('PROXYSQL_PASS')
}

print(f"dbconfig:{dbconfig}")


class Query:
    con = mysql.connector.connect(pool_name="PROXYSQL_POOL", pool_size=2, **dbconfig)

    def mysql_query(self, sql_text):
        try:
            with self.con.cursor() as cur:
                cur.execute(sql_text)
                row_headers = [x[0] for x in cur.description]
                for result in cur.fetchall():
                    yield dict(zip(row_headers, result))
        except mysql.connector.errors.OperationalError as err:
            if err.msg.startswith("MySQL Connection not available"):
                self.con = mysql.connector.connect(pool_name="PROXYSQL_POOL", pool_size=2, **dbconfig)
