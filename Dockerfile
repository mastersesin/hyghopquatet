FROM python:3.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD uwsgi --http :5001 --wsgi-file wsgi.py