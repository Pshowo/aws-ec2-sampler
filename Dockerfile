FROM python:3.9-slim

COPY requirements.txt .
RUN yum install python3 -y
RUN python3 -m pip install --upgrade pip --user
RUN python3 -m pip install -r requirements.txt


COPY . .

CMD python3 app.py