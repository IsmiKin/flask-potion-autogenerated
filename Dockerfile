FROM python:3.5
RUN apt-get update && apt-get install -y mariadb-client curl && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /pinfo
WORKDIR /pinfo

COPY requirements.txt /pinfo/
RUN pip install -r requirements.txt

COPY . /pinfo/

EXPOSE 4333

STOPSIGNAL SIGINT
ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "server.py"]
