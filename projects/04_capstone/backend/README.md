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
.\env\Scripts\activate.ps1
pip install -r requirements.txt
```

## How to launch application

1. Run the development server:

- MacOS/Linux

```shell
source env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
python app.py
```

- Windows with using PowerShell (in case of using 1 installed version of Python use **python**, otherwise use your version of **python3**)

```powershell
.\env\Scripts\activate.ps1
$env:FLASK_APP = 'app'
$env:FLASK_ENV = 'development'
python .\app.py
```

## References

- Mostly all packages of this project have their official documentation - please take a look at package documentation official links at [PYPI](https://pypi.org/)

- Additional information you can mostly always find at [StackOverflow](https://stackoverflow.com/)
