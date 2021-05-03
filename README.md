# Where to go

Web-app representing an interactive map with interesting points.

![Moscow roofs](https://i.ibb.co/kJ51dBB/roofs.png)

Link to [working site](https://balancy.pythonanywhere.com/)

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

5. Rename `.env.example` to `.env` and define your propre values for environmental variables:

- `DEBUG` — debug mode
- `SECRET_KEY` — project secret key
- `DATABASE_URL` — name of your DB
- `ALLOWED_HOSTS` — see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Launch

1. Make migrations
```console
python3 manage.py migrate
```

2. Run server
```console
python3 manage.py runserver
```

## Populate DB

It's possible to populate DB by command:
```console
python manage.py load_place <path_to_your_json_file>
```

## Project goals

Code is written for study purpose - for Python web-development course on [Devman](https://dvmn.org).