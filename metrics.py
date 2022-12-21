from prometheus_client.core import (CounterMetricFamily,
                                    GaugeMetricFamily)

from query import mysql_query

NAMESPACE = 'proxysql'


class StatsMysqlCommandsCountersCollector(object):
    """
    stats_mysql_commands_counters
    """
    name = "stats_mysql_commands_counters"

    def collect(self):
        for r in mysql_query('select * from stats_mysql_commands_counters'):
            r_command = r['command']
            c = CounterMetricFamily('', r_command, labels=['command'])
            for k, v in list(r.items())[1:]:
                c.name = f"{NAMESPACE}_{self.name}_{k}"
                c.add_metric(r_command, v)
                yield c
