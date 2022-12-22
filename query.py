import mysql.connector

oms_host = "192.168.161.18"
# oms_host = "proxysql"
oms_port = 6032


class Query:
    con = mysql.connector.connect(host=oms_host, port=oms_port, user='cadmin', password='cadmin')

    def check_conn(self,):
        with self.con.cursor() as cur:
            cur.execute("select 1")
            cur.fetchone()

    def mysql_query(self, sql_text):
        self.check_conn()
        # c = mysql.connector.connect(
        #     host=oms_host, port=oms_port, user='radmin', password='radmin')
        with self.con.cursor() as cur:
            cur.execute(sql_text)
            row_headers = [x[0] for x in cur.description]
            for result in cur.fetchall():
                yield dict(zip(row_headers, result))
# mysql_query('select * from stats_mysql_commands_counters')


# for i in mysql_query('select * from stats_mysql_commands_counters'):
#     print(i)
