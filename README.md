# Where to go

Web-app representing an interactive map with interesting points.

![Moscow roofs](https://i.ibb.co/kJ51dBB/roofs.png)

Link to [site]()

## Install

Python3 and Git should be already installed. 

1. Clone the repository by command:
```console
git clone https://github.com/balancy/where-to-go
```

2. Go inside cloned repository and create virtual environment by command:
```console
python -m venv env
```

3. Activate virtual environment. For linux-based OS:
```console
source env/bin/activate
```
&nbsp;&nbsp;&nbsp;
For Windows:
```console
env\scripts\activate
```

4. Install requirements by command:
```console
pip install -r requirements.txt
```

## Launch

1. Create your SQLite DB

2. Make migrations
```console
python3 manage.py migrate
```

3. Run server
```console
python3 manage.py runserver
```

## Environmental variables

Rename `.env.example` to `.env` and define your propre values for environmental variables:

- `DEBUG` — debug mode
- `SECRET_KEY` — project secret key
- `DATABASE_FILEPATH` — path to your SQLite DB
- `ALLOWED_HOSTS` — see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Project goals

Code is written for study purpose - for Python web-development course on [Devman](https://dvmn.org).