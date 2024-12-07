## CCT Dublin College

|                        |                                     |
|------------------------|-------------------------------------|
| **Module Title:**      | Secure Programming and Scripting    |
| **Assessment Title:**  | Build a secure authorization server |
| **Lecturer Name:**     | David Gonzalez                      |
| **Student Full Name:** | Javier Alfonso Ocampo               |
| **Student Number:**    | 2024328                             |


### The current flask application aims to work as example of a simple authorization server.

This server uses `flask` and `python` as a core and also some flask modules to power up the application. Also
`postgresql` as a database to store the users and `redis` for caching purpose to save the short lived token there for 10 minutes.
The server is containerize by using `Docker` and `Docker Compose`.

- `Flask-Bcrypt`: for password hashing, this library introduce the salt with a lenght of 12 by default.
- `Flask-SQLAlchemy`: this module help us to connect to the database, is a wrapper of SQLAlchemy, a common-used ORM.
- `Flask-JWT-Extended`: package for the generation of the JWT.
- `redis`: simple redis client.


### Server setup

In order to setting up the server, we need as a prerequisites the following tools:
- `Docker Engine`
- `Docker compose`

You can check the install instructions according to your OS in their [oficial documentaion](https://docs.docker.com/get-started/get-docker).


With that in place, the next step is just execute from the root folder `/auth-server` the following command `docker compose up -d`. This
command will pull and build the docker images needed to run the server, as also run the server itself. If everything is correct
you should be able to see three containers running, the flask application, postgres database and redis. Like follow:


```
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS          PORTS                                       NAMES
606e655d350d   auth-server-flask-app   "flask run --host=0.…"   31 minutes ago   Up 31 minutes   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   auth-server-flask-app-1
78f371752274   postgres:15             "docker-entrypoint.s…"   31 minutes ago   Up 31 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   postgres-db
c45550fb9dcc   redis:latest            "docker-entrypoint.s…"   31 minutes ago   Up 31 minutes   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   auth-server-redis-1
```

Now you are capable to navigate to `http://localhost:3000/register` to start testing the server. The routes availables are:

```
/register
/login
/protected
/access_token
/credentials
/create-user
```

### Steps to try the server

- Navigate to `http://localhost:3000/register` and add a new user by filling the form.
- Navigate to `http://localhost:3000/login` and enter the username and password from the user you just created.
- You will be redirected to a `https://cct-app.ie/?short_lived_token=80d5e0af-75f1-49b3-94ae-7d8e2baf9d1c`. This
website of course, dosen't exists, however it could be a potential application using our server. Please notice the short live token
as a part of the url in query string format.
- Copy the value of the `short_lived_token` in this example `80d5e0af-75f1-49b3-94ae-7d8e2baf9d1c`.
- Navigate to `http://localhost:3000/access_token?short_lived_token=80d5e0af-75f1-49b3-94ae-7d8e2baf9d1c`. Notice that
the short lived token was added as a part of the url too.
- A response with the `access_token` will be recieved. You can use that token to access to the protected information. Send the access token
as an Authroization Bearer token using tools like Curl or Postman.


### Stop the server

To stop the server execute the command `docker compose down`. This will delete the containers previously created. The database will persist
due to a volume which was defined into the `docker-compose.yml` file.
