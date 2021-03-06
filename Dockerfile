FROM python:3.7.5
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code


COPY . /code/
RUN python -m pip install -r  requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
