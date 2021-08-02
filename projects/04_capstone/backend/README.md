# Capstone Agency

## Prerequisites

**Initialize and activate a virtualenv using:**

- MacOS/Linux

```shell
python -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

- Windows

```powershell
python -m virtualenv env
.\env\bin\activate.ps1
pip install -r requirements.txt
```

## How to launch application

1. Run the development server:

- MacOS/Linux

```shell
export FLASK_APP=app
export FLASK_ENV=development
python app.py
```

- Windows with using PowerShell (in case of using 1 installed version of Python use **python**, otherwise use your version of **python3**)

```powershell
$env:FLASK_APP = 'app'
$env:FLASK_ENV = 'development'
python .\app.py
```

## References

- [Flask-RestPlus](https://flask-restplus.readthedocs.io/)
- [Python API: Authorization](https://auth0.com/docs/quickstart/backend/python/01-authorization)
