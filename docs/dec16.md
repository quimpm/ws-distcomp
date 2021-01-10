# Table of Contents

1.  [Coses a preguntar](#org5dfa4a0)
2.  [Notes de desenvolupament](#org25031b2)
3.  [Arquitectura](#orge9c9b57)
    1.  [Bàsics](#org8e43138)
    2.  [Advanced](#org92ca6d4)
    3.  [Integració](#orge985253)

![img](img/message_passing.png)

<a id="org5dfa4a0"></a>

# Coses a preguntar

- Sobre time i location (Exam)
- Datasource serveix per extraure el driver de connexió del servidor, i
  aixi poder canviar de base de dades. En el nostre cas ja ho fa SQLAlchemy
  (ORM), que extrau aquest tipus de connexio de SQLs. L&rsquo;abstracció de quina
  BD utilitzar ho farem desde l&rsquo;`.env`.
- Session es necessari? RMI qualsevol estudiant es pot connectar. Llavors,
  el Professor ha de dir els alumnes que es poden connectar? O mentre sigui
  un alumne es pot connectar al examen?

<a id="org25031b2"></a>

# Notes de desenvolupament

- Canviar delete dels tests d&rsquo;exam, només s&rsquo;ha de poder esborrar
  si no té grades.

<a id="orge9c9b57"></a>

# Arquitectura

<a id="org8e43138"></a>

## Bàsics

- Donar un identificador a l&rsquo;exam
- Guardar la descripció, la date/time i location
  &#x2014;
- Poder borrar l&rsquo;examen si no te cap nota
- Modificar la descripció de l&rsquo;examen
- S&rsquo;ha de poder buscar el contingut de l&rsquo;examen amb l&rsquo;id
  o la descripció parcial o sencera de l&rsquo;examen.
- s&rsquo;ha de poder descargar la informació de l&rsquo;examen per
  identificador o per llistant tots els examens

<a id="org92ca6d4"></a>

## Advanced

- S&rsquo;ha de poder posar notes a un examen.
- S&rsquo;ha de poder descarregar les notes d&rsquo;un estudiant.
- S&rsquo;ha de poder guardar i extreure tota la informació dels
  examens / teus examens.
- &#x2013; de la merda que utilitza
- S&rsquo;ha de poder gestionar l&rsquo; accés de l&rsquo;estudiant per id. (?)

<a id="orge985253"></a>

## Integració

- RMI ha de crear l&rsquo;examen al ws.
- Els estudiants han de validar l&rsquo;id abans de començar
  l&rsquo;examen. Els hi donarà detalls de la connexió amb el
  servidor.
- S&rsquo;ha de poder guardar les notes desde el WS.

`exam=exam_id`

<table id="org3665e2a" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Method</th>
<th scope="col" class="org-left">URL</th>
<th scope="col" class="org-left">What</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">get</td>
<td class="org-left">exam/</td>
<td class="org-left">List d&rsquo;exams</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Detall de Exam (tot)</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">exam/search?description={text}/</td>
<td class="org-left">Buscar descripció parcial.</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">exam/</td>
<td class="org-left">Crea exam. pk no s&rsquo;ha de donar.</td>
</tr>

<tr>
<td class="org-left">put</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Modificar camps d&rsquo;Exam (tots)</td>
</tr>

<tr>
<td class="org-left">patch</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Partial update.</td>
</tr>

<tr>
<td class="org-left">delete</td>
<td class="org-left">exam/{exam}/</td>
<td class="org-left">Deletes if professor and no grades</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">post</td>
<td class="org-left">grades/</td>
<td class="org-left">Penjar nota d&rsquo;un examen.</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">grades/{user}/user/</td>
<td class="org-left">List totes les notes d&rsquo;un estudiant.</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">grades/</td>
<td class="org-left">List all grades.</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Detail a grade.</td>
</tr>

<tr>
<td class="org-left">put</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Updates a grade.</td>
</tr>

<tr>
<td class="org-left">patch</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Partially updates a grade.</td>
</tr>

<tr>
<td class="org-left">delete</td>
<td class="org-left">grades/{grade<sub>id</sub>}</td>
<td class="org-left">Deletes a grade.</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">post</td>
<td class="org-left">auth/login/</td>
<td class="org-left">Logins</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">auth/logout/</td>
<td class="org-left">Logouts</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/logout/</td>
<td class="org-left">Logout</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/password/change/</td>
<td class="org-left">Password change.</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/password/reset/</td>
<td class="org-left">Password reset by email confirmation. Needs Email configuration</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/password/reset/confirm/</td>
<td class="org-left">Password Confirmation</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/registration/</td>
<td class="org-left">Register a new user.</td>
</tr>

<tr>
<td class="org-left">post</td>
<td class="org-left">auth/registration/verify-email</td>
<td class="org-left">Verifies email. Needs Email configuration</td>
</tr>

<tr>
<td class="org-left">get</td>
<td class="org-left">auth/user/</td>
<td class="org-left">Reads User. Needs authentication</td>
</tr>

<tr>
<td class="org-left">put</td>
<td class="org-left">auth/user/</td>
<td class="org-left">Updates User</td>
</tr>

<tr>
<td class="org-left">patch</td>
<td class="org-left">auth/user/</td>
<td class="org-left">Partial update.</td>
</tr>
</tbody>
</table>  

# Screenshots
The screenshots are for the most important cases, there are endpoints
that has been omitted, like user password change.

## Authentication
+ Register
![img](img/registration.png)
+ Login
![img](img/login.png)

## Exam
+ List exams
![img](img/list_exams.png)
+ Create exam
![img](img/create_exam.png)
+ Read exam
![img](img/read_exam.png)
+ Update exam
![img](img/update_exam.png)
+ Patch exam
![img](img/partial_update_exam.png)
+ Delete exam
![img](img/delete_exam.png)
+ Search exam
![img](img/search1.png)

## Grades
+ List grades
![img](img/list_grades.png)
+ Create grade
![img](img/create_grades.png)
+ Read grade
![img](img/get_grades_by_id.png)
+ Update grade
![img](img/update_grade.png)
+ Patch grade
![img](img/patch_grade.png)
+ Delete grade
![img](img/delete_grade.png)
+ Search user grades
![img](img/get_user_grade.png)
+ Search exam grades
![img](img/get_exam_grade.png)

# How To

# Solution justification
## Web Service

### Technologies
+ Django: We have chosen this technology because our familiarity with it and
  its ease to work with data models and ORM.
+ Django rest framework: this framework is a powerfull and easy-to-use tool 
  for building web REST API's, it includes mechanisms for searialization and
  authentication, which we found necessary.
+ SQLite: it is the Django default database (a postgres database is also 
  configured using docker) 
+ Docker: It facilitates the configuration and portabiltiy of the project.

###  Decisions
+ **Authentication**: we developed a simple autenticathon in which users
  once registered and logged are provided with a token that they will need
  to make specific api calls. There are custom permisions to prevent forbidden
  actions, like a student deleting an exam, or modifiying a grade.
  We used django_rest_auth, which provides endpoints for registration, authentication,
  password resset, retrieve and update user details, etc.

+ **Get user**:  <!-- TODO: S'ha de comentar? -->

## RMI modifications
+ **HTTP**: We have made two adapter classes in order to encapsulate the http
  requests made to the web service by the client and the server.
  To make the request we have used OkHttp3, we were restricted to use a library
  from before java 8 because of RMI deprecation. We were unable to mock and 
  test the api calls because OkHttp3 Request and Response object does not implement
  equals, and are final.
+ **Client flow changes**: Now the client has to be identified in order to enter the
  exam session, so the first step is to ask for a correct user and password. Once
  authenticated correctly the user is given 3 options:
  - **search \<keywords>** : searches exams by its description and outputs the information of the matched exams.
  - **list** : lists and outputs all the exams and its information.
  - **choose \<id_exam>** : chose the desired exam in order to connect to its session.
  Once an exam is chosen, the flow works as before.

+ **Server flow changes**: As happens with the client, the professor has to be identified in
  order to create an exam session, so the first step is to ask for a correct user and password.
  Once authenticated correctly it will be asked to introduce the following parametters in order
  to create the exam:
  - **description**: the desription of the exam.
  - **date**: the date of the exam, it needs a specific date format,  as 2021-01-11T14:00:00Z.
  - **location**: the location of the exam (string). We decided that the location will be 
    the bind key of the remote object that references that exact exam session. 
  Once the last parammeter is filled, the exam will be created in the web service, as well as
  the session in which the students can connect to perform the exam. When the professor 
  finnishes the exam all the grades are updated to the web service.


## Hours dedicated
It is difficult to say, but we estimate an approximate of 90 hours.
We are a group of three students, and we worked in this project 
for 6 days, 5 hours each day.
