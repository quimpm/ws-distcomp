# Table of Contents

1.  [Coses a preguntar](#org30881c7)
2.  [Notes de desenvolupament](#org04405c5)
3.  [Arquitectura](#orgd3ce228)
    1.  [Bàsics](#orgb1e9f54)
    2.  [Advanced](#org1bc96ae)
    3.  [Integració](#org452ae4d)

![img](img/message_passing.png)

<a id="org30881c7"></a>

# Coses a preguntar

- Sobre time i location (Exam)
- Datasource serveix per extraure el driver de connexió del servidor, i
  aixi poder canviar de base de dades. En el nostre cas ja ho fa SQLAlchemy
  (ORM), que extrau aquest tipus de connexio de SQLs. L&rsquo;abstracció de quina
  BD utilitzar ho farem desde l&rsquo;`.env`.
- Session es necessari? RMI qualsevol estudiant es pot connectar. Llavors,
  el Professor ha de dir els alumnes que es poden connectar? O mentre sigui
  un alumne es pot connectar al examen?

<a id="org04405c5"></a>

# Notes de desenvolupament

- Canviar delete dels tests d&rsquo;exam, només s&rsquo;ha de poder esborrar
  si no té grades.

<a id="orgd3ce228"></a>

# Arquitectura

<a id="orgb1e9f54"></a>

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

<a id="org1bc96ae"></a>

## Advanced

- S&rsquo;ha de poder posar notes a un examen.
- S&rsquo;ha de poder descarregar les notes d&rsquo;un estudiant.
- S&rsquo;ha de poder guardar i extreure tota la informació dels
  examens / teus examens.
- &#x2013; de la merda que utilitza
- S&rsquo;ha de poder gestionar l&rsquo; accés de l&rsquo;estudiant per id. (?)

<a id="org452ae4d"></a>

## Integració

- RMI ha de crear l&rsquo;examen al ws.
- Els estudiants han de validar l&rsquo;id abans de començar
  l&rsquo;examen. Els hi donarà detalls de la connexió amb el
  servidor.
- S&rsquo;ha de poder guardar les notes desde el WS.

`exam=exam_id`

<table id="org875eb5a" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

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
<td class="org-left">grades/user/{user}/</td>
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
