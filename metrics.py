from datetime import datetime, timedelta
import time

from prometheus_client.core import CounterMetricFamily

from query import Query

NAMESPACE = 'proxysql'


q = Query()


class StatsMysqlCommandsCountersCollector(object):
    """
    stats_mysql_commands_counters
    """
    name = "stats_mysql_commands_counters"

    def collect(self):
        c = CounterMetricFamily(f"{NAMESPACE}_{self.name}", "", labels=['command', 'type'])
        for r in q.mysql_query('select * from stats_mysql_commands_counters'):
            r_command = r['Command']
            for k, v in list(r.items())[1:]:
                c.add_metric([r_command, k.lower()], v)
        yield c


class StatsMysqlQueryDigest(object):
    """
    stats_mysql_query_digest
    """
    name = "stats_mysql_query_digest"
    labels = [
        'hostgroup',
        'schemaname',
        "username",
        "digest",
        "metric"
    ]

    def collect(self):
        ini_time_for_now = time.mktime(datetime.now().timetuple())
        last_seen = int(ini_time_for_now - 3600)  # 86400
        c = CounterMetricFamily(f"{NAMESPACE}_{self.name}", "", labels=self.labels)
        for r in q.mysql_query(f'select hostgroup, schemaname, username, digest, count_star, sum_time, sum_rows_affected, sum_rows_sent from stats_mysql_query_digest where last_seen >= {last_seen}'):
            for k, v in list(r.items()):
                if k in ['count_star', 'sum_time', 'sum_rows_affected', 'sum_rows_sent']:
                    c.add_metric([r['hostgroup'], r['schemaname'], r['username'], r['digest'], k], v)
        yield c
