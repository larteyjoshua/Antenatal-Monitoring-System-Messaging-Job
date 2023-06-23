FROM python:3.10-alpine

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
COPY ./.env /src/.env

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./app /src/app
COPY ./run.py /src/run.py

EXPOSE 80
CMD ["python", "run.py"]