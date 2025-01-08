FROM python:3.9.20-alpine3.20

WORKDIR /app

COPY ./flask-app.py /app/

RUN pip install flask

CMD [ "python3", "flask-app.py" ]

EXPOSE 5000