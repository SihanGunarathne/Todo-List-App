# FROM python:3.10
# EXPOSE 5000
# #RUN mkdir /app
# WORKDIR /app

# COPY . .

# #COPY requirements.txt /app
# #COPY app/requirements.txt /app

# RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py .

# CMD python app.py





FROM python:3.10

EXPOSE 5000

WORKDIR /app

# COPY requirements.txt .
COPY app/ .

RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py .

CMD ["python", "app.py"]
