# tms
Task Management System

# Installation
1 - git clone https://github.com/dev-omaribrahim/tms.git

2 - create virtualenv & activate it

3 - cd tms

4 - create .env file on root dir

5 - add env vars:

    SECRET_KEY=<Your Django Secret Key>
    DEBUG=<True Or False>
    ALLOWED_HOSTS=<Your Allowed Hosts>
    DATABASE_URL=<DB URL>
    LOGS_FILE_NAME=<Log File Name>

6 - pip install -r requirements.txt

7 - python manage.py makemigrations

8 - python manage.py migrate

9 - python manage.py createsuperuser


# run

1 - python manage.py runserver
