# Full Stack Trivia API Backend

## Python 3.7

- Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
- Please also install pip3 with Python

## Create Virtual Environment

```shell
pip3 install virtualenv
python -m virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Database Setup

- set **TRIVIA_DB_USERNAME** and **TRIVIA_DB_PASSWORD** in your environment for your database

```shell
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```shell
export FLASK_APP=app
export FLASK_ENV=development
python .\app.py
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## API Documentation

- Open url [API_DOCS](http://localhost:5000/docs) after started server (you can also make requests with Swagger)

## Testing

- set **TRIVIA_DB_USERNAME** and **TRIVIA_DB_PASSWORD** in your environment for your database

To run the tests, run

```shell
dropdb trivia_test
createdb trivia_test
python .\tests\test_flaskr.py
```
