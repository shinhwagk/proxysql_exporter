FROM python:3.11-slim as builder
COPY requirements.txt .
RUN pip install --target=/install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
WORKDIR app
COPY main.py metrics.py query.py /app

FROM python:3.11-slim as app
COPY --from=builder /install /usr/local/lib/python3.11/site-packages/
COPY --from=builder /app /app
CMD python /app/main.py