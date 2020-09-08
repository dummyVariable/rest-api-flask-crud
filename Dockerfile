FROM python

COPY ./api /app/api
COPY app.py /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]