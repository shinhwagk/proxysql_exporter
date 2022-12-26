```sh
export PROXYSQL_HOST=192.168.161.18
export PROXYSQL_PORT=6032
export PROXYSQL_USER=cadmin
export PROXYSQL_PASS=cadmin
/usr/local/bin/python /workspaces/proxysql_exporter/main.py


docker build -t shinhwagk/proxysql_exporter:0.0.2
```