FROM python:3.10
EXPOSE 5000
RUN mkdir /app
WORKDIR /app

COPY app/ .

#COPY requirements.txt /app
COPY app/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

#COPY app.py /app
COPY app.py /app

CMD python app.py
