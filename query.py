import os

import mysql.connector


class Query:
    con = mysql.connector.connect(host=os.getenv('PROXYSQL_HOST'), port=os.getenv('PROXYSQL_PORT'), user=os.getenv('PROXYSQL_USER'), password=os.getenv('PROXYSQL_PASS'))

    def check_conn(self,):
        with self.con.cursor(buffered=True) as cur:
            cur.execute("select 1")

    def mysql_query(self, sql_text):
        self.check_conn()
        with self.con.cursor() as cur:
            cur.execute(sql_text)
            row_headers = [x[0] for x in cur.description]
            for result in cur.fetchall():
                yield dict(zip(row_headers, result))
