FROM python:3.10

WORKDIR /API

COPY . /API/

RUN pip install -r requirements.txt

CMD ["python","./API_Server_v2.py","&","python","enrichment.py","&","0 0 */2 * *  python","deletion.py"]
