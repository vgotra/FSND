# Coffee Shop Backend

## Python 3.9

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

- if you need to have new database or run tests in PostMan please uncomment line in **app.py**
```python
# db_drop_and_create_all()
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

## Tests

- Please use the latest version of PostMan (json file with tests exported to format 2.1)
- all token fully removed from tests for PostMan
