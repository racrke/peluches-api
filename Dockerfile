FROM python:3.7.3

ENV PYTHONUNBUFFERED True

WORKDIR /home/ecaresoft/reports

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY start.sh .
COPY server.py .
COPY app ./app
COPY db.json .
RUN chmod +x start.sh

CMD ["bash", "start.sh"]