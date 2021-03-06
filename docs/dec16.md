# Activity 6: WS Project

**Github:** [WS Project](https://github.com/quimpm/ws-distcomp), [RMI Project](https://github.com/sergisi/java-rmi/tree/integration)

**Made by:** Sergi Simón Balcells, Ian Palacín Aliana, Joaquim Picó Mora

**Date:** Dilluns 11/01/2020

**Subject:** Distributed Computing

**Professor:** Jordi Gervás Arruga

**Universitat de Lleida**

# Introduction

In this document is it specified all the endpoints and which responses do they
return, as well as a defense of which technologies we have used.

Additionally, it can be found a table containing the rest api developed, as
well as a class diagram of the model of data used in the API.

# UML

![img](img/message_passing.png)

## Exam

Exam is the class that holds all the Exam information. It stores the description, the date and the location of the exam.

## User

User is the class that stores the information of the user that is making use of our system. It's the default implementation of the django User class.

## Grades

This class it's the one that stores grades of exams made by users.

# Endpoint Table

<table id="org3665e2a" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Method</th>
<th scope="col" class="org-left">URL</th>
<th scope="col" class="org-left">What</th>
<th scope="col" class="org-left">Status code</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">get</td>
<td class="org-left">exam/</td>
<td class="org-left">List d&rsquo;exams</td>
<td class="org-left">200</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Detall de Exam (tot)</td>
<td class="org-left">200, 404</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">exam/search?description={text}/</td>
<td class="org-left">Buscar descripció parcial.</td>
<td class="org-left">200</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">exam/</td>
<td class="org-left">Crea exam. pk no s&rsquo;ha de donar.</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">put</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Modificar camps d&rsquo;Exam (tots)</td>
<td class="org-left">200, 403, 401</td>
</tr>

<tr>
<td class="org-left">patch</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Partial update.</td>
<td class="org-left">200, 403, 401</td>
</tr>

<tr>
<td class="org-left">delete</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Deletes if professor and no grades</td>
<td class="org-left">204, 403, 401</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">post</td>
<td class="org-left">grades/</td>
<td class="org-left">Penjar nota d&rsquo;un examen.</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">grades/{user}/user/</td>
<td class="org-left">List totes les notes d&rsquo;un estudiant.</td>
<td class="org-left">200</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">grades/</td>
<td class="org-left">List all grades.</td>
<td class="org-left">200</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Detail a grade.</td>
<td class="org-left">200, 404</td>
</tr>

<tr>
<td class="org-left">put</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Updates a grade.</td>
<td class="org-left">200, 403, 401</td>
</tr>

<tr>
<td class="org-left">patch</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Partially updates a grade.</td>
<td class="org-left">200, 403, 401</td>
</tr>

<tr>
<td class="org-left">delete</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Deletes a grade.</td>
<td class="org-left">204, 403, 401</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">post</td>
<td class="org-left">auth/login/</td>
<td class="org-left">Logins</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">auth/logout/</td>
<td class="org-left">Logouts</td>
<td class="org-left">200</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/logout/</td>
<td class="org-left">Logout</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/password/change/</td>
<td class="org-left">Password change.</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/password/reset/</td>
<td class="org-left">Password reset by email confirmation. Needs Email configuration</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/password/reset/confirm/</td>
<td class="org-left">Password Confirmation</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/registration/</td>
<td class="org-left">Register a new user.</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/registration/verify-email</td>
<td class="org-left">Verifies email. Needs Email configuration</td>
<td class="org-left">201, 403, 401</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">auth/user/</td>
<td class="org-left">Reads User. Needs authentication</td>
<td class="org-left">200</td>
</tr>

<tr>
<td class="org-left">put</td>
<td class="org-left">auth/user/</td>
<td class="org-left">Updates User</td>
<td class="org-left">200, 403, 401</td>
</tr>

<tr>
<td class="org-left">patch</td>
<td class="org-left">auth/user/</td>
<td class="org-left">Partial update.</td>
<td class="org-left">200, 403, 401</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">get</td>
<td class="org-left">user/{user}/</td>
<td class="org-left">Gets user with pk.</td>
<td class="org-left">200, 404</td>
</tr>
</tbody>
</table>

# Screenshots

The screenshots are for the most important cases, there are endpoints
that has been omitted, like user password change.

Note that due to a bug in the docs viewer, as deleting an object only
returns a status code without any data, it does not correcly show that
the status code is 204. Instead, only shows "undefined", even though it
is properly deleted from the database.

## Authentication

- Register
  ![img](img/registration.png)
- Login
  ![img](img/login.png)

## Exam

- List exams
  ![img](img/list_exams.png)
- Create exam
  ![img](img/create_exam.png)
- Read exam
  ![img](img/read_exam.png)
- Update exam
  ![img](img/update_exam.png)
- Patch exam
  ![img](img/partial_update_exam.png)
- Delete exam
  ![img](img/delete_exam.png)
- Search exam
  ![img](img/search1.png)

## Grades

- List grades
  ![img](img/list_grades.png)
- Create grade
  ![img](img/create_grades.png)
- Read grade
  ![img](img/get_grades_by_id.png)
- Update grade
  ![img](img/update_grade.png)
- Patch grade
  ![img](img/patch_grade.png)
- Delete grade
  ![img](img/delete_grade.png)
- Search user grades
  ![img](img/get_user_grade.png)
- Search exam grades
  ![img](img/get_exam_grade.png)

# How To

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

DATABASE_URL="postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_NAME"

EMAIL_OPTION=none
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='mail@gmail.com'
EMAIL_HOST_PASSWORD='password1234'
EMAIL_PORT=587

```

Then apply the changes to you database using:

```
docker-compose up -d
docker-compose exec web python3 manage.py makemigrations
docker-compose exec web python3 manage.py migrate
docker-compose down
```

To create a super user, use:

```
docker-compose up -d
docker-compose exec web python3 manage.py createsuperuser
docker-compose down
```

Then use `docker-compose up -d` to get it running.
Connect to `localhost:8000/admin` to see the admin login
page, or `localhost:8000/docs` to see the docs.

To stop it, use `docker-compose down`

## Running the tests

To execute all tests, use
`docker-compose exec web python3 manage.py test`

# Solution justification

## Web Service

### Technologies

- Django: We have chosen this technology because our familiarity with it and
  its ease to work with data models and ORM.
- Django rest framework: this framework is a powerfull and easy-to-use tool
  for building web REST API's, it includes mechanisms for searialization and
  authentication, which we found necessary.
- SQLite: it is the Django default database. A postgres database can be
  configured as a replacement for scalability and deployment purposes, and
  is it already specified in the environment, but was left as SQLite was
  suffieciently for the requirements.
- Docker: It facilitates the configuration and portabiltiy of the project.
- Docker-compose: It facilitates even more the configuration of a docker.

### ViewSets and Generics

Django is an opinionated framework. With this, it provides powerfull abstraction
if you can manage to use them. Django REST Framework, based on it, _copies_ some
of their abstractions and provides them for a RESTful API. For example, in Django
we extend View classes and add them some information about which HTML
template to use and which database model, and it will pass correcly the data.

With the REST framework, we have a similar idea. We have the concept of generics,
that provides a unique endpoint to an action, as retrieving an object from the
database or listing a few of them. When they did this, they saw that most of their
implementations used the same parameters: where to get the objects and how to serialize
them. And for this reason they build what they called "ViewSets". ViewSets provide
an abstraction to build all the CRUD operations of a model in the database. In conjuntion
with the permissions class, they can provide a quick and robust way to deploy the API.
Most of our endpoints are made with this ViewSets. Filtering Views were made as custom
ListAPIViews with a custom get_queryset function.

### Decisions

- **Authentication**: we developed a simple autenticathon in which users
  once registered and logged are provided with a token that they will need
  to make specific api calls. There are custom permisions to prevent forbidden
  actions, like a student deleting an exam, or modifiying a grade.
  We used dj-rest-auth, which provides endpoints for registration, authentication,
  password resset, retrieve and update user details, etc.

  We also used django-all-auth, which provides a powerfull backend to registration.
  It also provides with a plug-and-play of social authentication,
  (i.e.: login with your Google account), and email verification. Although we
  initially made an Email backend, we needed to provide in the environment
  either a usable email or an email provider. We made a special parameter
  so they are not needed, as we thought that this will cause some trouble
  when correcting the project, rather than beiing a feature.

## RMI modifications

- **HTTP**: We have made two adapter classes in order to encapsulate the http
  requests made to the web service by the client and the server.
  To make the request we have used OkHttp3, we were restricted to use a library
  from before java 8 because of RMI deprecation. We were unable to mock and
  test the api calls because OkHttp3 Request and Response object does not implement
  equals, and are final.
- **Client flow changes**: Now the client has to be identified in order to enter the
  exam session, so the first step is to ask for a correct user and password. Once
  authenticated correctly the user is given 3 options:

  - **search \<keywords>** : searches exams by its description and outputs the information of the matched exams.
  - **list** : lists and outputs all the exams and its information.
  - **choose \<id_exam>** : chose the desired exam in order to connect to its session.
    Once an exam is chosen, the flow works as before.

- **Server flow changes**: As happens with the client, the professor has to be identified in
  order to create an exam session, so the first step is to ask for a correct user and password.
  Once authenticated correctly it will be asked to introduce the following parametters in order
  to create the exam:
  - **description**: the desription of the exam.
  - **date**: the date of the exam, it needs a specific date format, as 2021-01-11T14:00:00Z.
  - **location**: the location of the exam (string). We decided that the location will be
    the bind key of the remote object that references that exact exam session.
    Once the last parammeter is filled, the exam will be created in the web service, as well as
    the session in which the students can connect to perform the exam. When the professor
    finnishes the exam all the grades are updated to the web service.

## Hours dedicated

It is difficult to say, but we estimate an approximate of 90 hours.
We are a group of three students, and we worked in this project
for 6 days, 5 hours each day.
