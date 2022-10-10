# django-divichild-builder
## Gera arquivos de tema filho para o Divi do Wordpress utilizando Django

### Live demo
https://django-divichild-builder.herokuapp.com/

[![Updates](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/)
[![Build Status](https://travis-ci.org/tiagocordeiro/django-divichild-builder.svg?branch=master)](https://travis-ci.org/tiagocordeiro/django-divichild-builder)
[![codecov](https://codecov.io/gh/tiagocordeiro/django-divichild-builder/branch/master/graph/badge.svg)](https://codecov.io/gh/tiagocordeiro/django-divichild-builder)
[![Python 3.10.7](https://img.shields.io/badge/python-3.10.7-blue.svg)](https://www.python.org/downloads/release/python-3107/)
[![Django 4.1.2](https://img.shields.io/badge/django-4.1.2-blue.svg)](https://www.djangoproject.com/download/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/tiagocordeiro/django-divichild-builder/blob/master/LICENSE)

### Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
* Rode o projeto

```
git clone https://github.com/tiagocordeiro/django-divichild-builder.git
cd django-divichild-builder
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py runserver
```

Thanx to https://pyup.io/