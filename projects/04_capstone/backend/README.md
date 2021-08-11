# Capstone Agency

Project with some data related to typical company which is creating movies and managing actors

## Prerequisites

- Install PostgreSQL database, Python, Angular, Node, etc.

- Create a local database and set connection string in Environment variable (**DATABASE_URL**) in format usable for Alchemy and PostgreSQL

- Create account at Heroku and Github or other

- Initialize and activate a virtualenv using:

MacOS/Linux

```shell
python -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Windows with using PowerShell (in case of using 1 installed version of Python use **python**, otherwise use your version of **python3**)

```powershell
python -m virtualenv env
.\env\Scripts\activate.ps1
pip install -r requirements.txt
```

- Setup account at Auth0 with all permissions and roles, etc.

- Use flask migrate commands to migrate database structure (docs at flask migrate official site)

- Launch application

## How to launch application

- Run the development server:

MacOS/Linux

```shell
source env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
python app.py
```

Windows with using PowerShell (in case of using 1 installed version of Python use **python**, otherwise use your version of **python3**)

```powershell
.\env\Scripts\activate.ps1
$env:FLASK_APP = 'app'
$env:FLASK_ENV = 'development'
python .\app.py
```

## Unit Tests

- How to run unit tests:

MacOS/Linux

```shell
source env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
pytest
```

Windows with using PowerShell (in case of using 1 installed version of Python use **python**, otherwise use your version of **python3**)

```powershell
.\env\Scripts\activate.ps1
$env:FLASK_APP = 'app'
$env:FLASK_ENV = 'development'
pytest
```

## References

- Mostly all packages of this project have their official documentation - please take a look at package documentation official links at [PYPI](https://pypi.org/)

- Additional information you can mostly always find at [StackOverflow](https://stackoverflow.com/)
