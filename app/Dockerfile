FROM python:3.10
EXPOSE 5000
WORKDIR /app

#COPY requirements.txt /app
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#COPY app.py /app
COPY app/app.py .

CMD python app.py
