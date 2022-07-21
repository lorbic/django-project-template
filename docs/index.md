# Django-project-template by Lorbic

This repository is preconfigured django project with following features:

1. Custom user model with `email` as default username field.
2. Database server configuration.
3. Email server configuration.
4. Environment variables are managed using `.env` file.

> Copy &nbsp; `sample_dot_env`&nbsp; to &nbsp;`.env`&nbsp; and change the values


## Development 

#### 👉 Install the dependencies
```sh
pip install -r requirements.txt
```
#### 👉 Edit the `.env` file and define the env variables.
#### 👉 Run tests.
```sh
python manage.py test
```
#### 👉 Run the webserver.
```sh
python manage.py runserver
```

#### 👉 You may need to create database migrations.
```sh
python manage.py makemigrations

python manage.py migrate
```


## Resources
This project uses [python-decouple-3.6](https://github.com/henriquebastos/python-decouple) for configuration (environment variable) management.

