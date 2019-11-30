FROM python:2.7

WORKDIR /usr/app

# add requirements
COPY ./requirements.txt ./

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# add files
COPY . .

# run server
CMD python manage.py runserver 0.0.0.0:2000