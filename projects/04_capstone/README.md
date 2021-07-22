# Capstone Agency

## Prerequisites

**Initialize and activate a virtualenv using:**

- MacOS/Linux
```shell
python -m virtualenv env
source env/bin/activate
```

- Windows
```powershell
python -m virtualenv env
.\env\bin\activate.ps1
```

## How to launch application

1. Initialize and activate a virtualenv using (according to previous steps explained in README) and install the dependencies:

```shell
pip install -r requirements.txt
```

2. Create a database in PostgreSQL with username and login specified in connection string can be found in **config.py**

3. Apply database migrations to database:

```shell
flask db migrate
```

4. Run the development server:

- MacOS/Linux

```shell
export FLASK_APP=app
export FLASK_ENV=development # enables debug mode
python3 app.py
```

- Windows with using PowerShell (in case of using 1 installed version of Python use **python**, otherwise use your version of **python3**)
```powershell
$env:FLASK_APP = 'app'
$env:FLASK_ENV = 'development'
python .\app.py
```

## References

- [Blueprints and views](https://flask.palletsprojects.com/en/2.0.x/tutorial/views/#blueprints-and-views)