```sh
export PROXYSQL_HOST=192.168.161.18
export PROXYSQL_PORT=6032
export PROXYSQL_USER=cadmin
export PROXYSQL_PASS=cadmin
/usr/local/bin/python /workspaces/proxysql_exporter/main.py


docker build -t shinhwagk/proxysql_exporter:0.0.2 .


docker run --name=proxysql_exporter_node1 -p 9888:8000 -d -e PROXYSQL_HOST=172.23.8.37 -e PROXYSQL_PORT=6032 -e PROXYSQL_USER=exporter -e PROXYSQL_PASS=exporter shinhwagk/proxysql_exporter:0.0.2

docker run --name=proxysql_exporter -p 9888:8000 -d -e PROXYSQL_HOST=172.23.8.387 -e PROXYSQL_PORT=6032 -e PROXYSQL_USER=exporter -e PROXYSQL_PASS=exporter shinhwagk/proxysql_exporter:0.0.2
```