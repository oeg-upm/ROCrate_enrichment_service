FROM python:3.10

WORKDIR /API

COPY . /API/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y cron

EXPOSE 5000
CMD ["python","run.py"]

