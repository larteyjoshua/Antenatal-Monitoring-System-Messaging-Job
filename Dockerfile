FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
COPY .env /app/.env
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 80
CMD ["python3", "run.py"]