FROM python
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ./api /app/api
COPY app.py /app

CMD [ "python", "app.py" ]