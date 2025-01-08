# flask-exporter
Счетчик посещений страницы

Run command: `docker run -p 5000:5000 helby255/flask-visitors`

-app объявляет переменную без которой не будет работать
--host 0.0.0.0 слушает отовсюду (доверенные адреса)

Go to URL: `127.0.0.1:5000/metrics`

See also: https://hub.docker.com/r/helby255/flask-visitors