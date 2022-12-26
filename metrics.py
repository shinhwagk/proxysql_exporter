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
        for r in q.mysql_query('select * from stats_mysql_commands_counters'):
            r_command = r['Command']
            for k, v in list(r.items())[1:]:
                c = CounterMetricFamily(f"{NAMESPACE}_stats_mysql_commands_counters", r_command, labels=['command', 'type'])
                c.add_metric([r_command, k.lower()], v)
                yield c
