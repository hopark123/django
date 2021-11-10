RUN /usr/src/app/manage.py makemigrations
RUN /usr/src/app/manage.py migrate
RUN /usr/src/app/manage.py runserver
