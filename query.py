import mysql.connector

oms_host = "192.168.161.18"
oms_port = 6032


def mysql_query(sql_text):
    c = mysql.connector.connect(
        host=oms_host, port=oms_port, user='cadmin', password='cadmin', charset='utf8', collation='utf8_general_ci')
    # with mysql.connector.connect(host=oms_host, port=oms_port, user='cadmin', password='cadmin') as con:
    #     con.set_charset_collation('utf8', 'utf8_general_ci')
    #     print(con.get_server_info())

    # with con.cursor() as cur:
    #     cur.execute(sql_text)
    #     row_headers = [x[0] for x in cur.description]
    #     for result in cur.fetchall():
    #         yield dict(zip(row_headers, result))
mysql_query('select * from stats_mysql_commands_counters')

# for i in mysql_query('select * from stats_mysql_commands_counters'):
#     print(i)
