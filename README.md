# ws-distcomp

## Getting Started

These instructions will get you a copy of the project up
and running on your local machine for development and
testing purposes. See deployment for notes on how to
deploy the project on a live system.

### Prerequisites

You will need to have installed docker and docker-compose.
To know if this is working properly use
`docker run hello-world` and `docker-compose --version`.
To get them installed properly at your OS,
refer to the oficial pages of docker and use:

```
python3 -m pip install docker-compose
```

### Installing

Copy '.env.example' to file named '.env'. Then change
the variable `DJANGO_SECRET_KEY=[key]` to a value generated.
For example, using [this site](https://miniwebtool.com/django-secret-key-generator/).

So the contents of .env should be:

```
#Django configuration

OPEN_PORT=8000
DJANGO_PORT=8000

DJANGO_SECRET_KEY=<your secret key goes here>
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 0.0.0.0

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_NAME=postgres

DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```

Then apply the changes to you database using:

```
docker-compose exec web python3 manage.py makemigrations
docker-compose exec web python3 manage.py migrate
```

To create a super user, use:
`docker-compose exec web python3 manage.py createsuperuser`

Then use `docker-compose up -d` to get it running. Connect to `localhost:8000/admin`
to see the admin login page, or `localhost:8000/docs` to see the docs.

To stop it, use `docker-compose down`

## Running the tests

To execute all tests, use `docker-compose exec web python3 manage.py test`

### Test Structure

Tests are in these format:

```
apps
  | ...
  | tests
    | __init__.py
    | test_<something>.py
```

So we ensure that all tests are discovered and tests are separated for diferent
functionalities, as models, views or templates.

### Test names

All tests must be using a class derived from TestCase (or derived from it). Also,
all methods that test must begin with test, so manage.py does properly discover them.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used.
- [Docker](https://www.docker.com/) - Container management.
- [SQLite](https://sqlite.org/index.html) - Open Source Database.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Makes Django a REST framework
- [Dj-rest-auth](https://github.com/jazzband/dj-rest-auth) - Gets a secure API for authentication
- [Django All auth](https://django-allauth.readthedocs.io/en/latest/installation.html) - Secure Registration Implementation. Has many social adaptors.

## Authors

- Ian Palacín Aliana
- Joaquim Picó Mora
- Sergi Simón Balcells

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
