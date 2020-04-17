# URL Status Checker

## Installation

Create a virtual environment and activate it.

```bash
python3 -m venv env
source env/bin/activate
```

Run all Django migrations.

```bash
python3 manage.py migrate
```

Create a superuser.

```bash
python3 manage.py createsuperuser
```

Run a development server.

```bash
python3 manage.py runserver.
```

Open [this link](http://127.0.0.1:8000/admin/) in a browser and login in Django admin panel and create few links.
After that go to [user list page](http://127.0.0.1:8000/urls/) and test status of your urls.
