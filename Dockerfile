FROM python:3.12.9

WORKDIR /app

COPY /src .

RUN pip install -r requirements.txt


CMD [ "python", "manage.py", "runserver", "0.0.0.0:80", "--noreload" ]