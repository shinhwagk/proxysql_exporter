import random
import time

from prometheus_client import Summary, start_http_server
from prometheus_client.core import REGISTRY

from metrics import StatsMysqlCommandsCountersCollector

REGISTRY.register(StatsMysqlCommandsCountersCollector())


REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    start_http_server(8000)
    print("start.")
    while True:
        process_request(random.random())
