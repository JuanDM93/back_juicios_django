# Back-Juicios

Python-based Django system

## Installation

Once cloned, create new [python environment](https://docs.python.org/3/tutorial/venv.html) 'env', activate it and install reqs

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Build and [migrate](https://docs.djangoproject.com/en/3.1/topics/migrations/) DB

```bash
python manage.py makemigrations accounts locals federals
python manage.py migrate
```

## Usage

Create admin user

```bash
python manage.py createsuperuser
```

Run service

```bash
python manage.py runserver <PORT>
```

## APIs

Admin (baseURL/admin)

Users (baseURL/accounts)

```bash
../abogados
../despachos
```

Locales (baseURL/locals)

```bash
../acuerdos
../juicios
../juzgados
```

Federal (baseURL/federals)

```bash
../acuerdos
../juicios
../juzgados
```

## Contributing

For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)