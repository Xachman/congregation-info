FROM python

RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib flask

WORKDIR /app
COPY . /app

CMD python app.py