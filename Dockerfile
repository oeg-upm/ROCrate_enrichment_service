FROM alpine:3.10


WORKDIR /API

COPY . /API/
RUN apk add --no-cache python3-dev 
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 5000
CMD ["python3","run.py"]

