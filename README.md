# django-divichild-builder
## Gera arquivos de tema filho para o Divi do Wordpress utilizando Django


[![Updates](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/django-divichild-builder/)
[![Build Status](https://travis-ci.org/tiagocordeiro/django-divichild-builder.svg?branch=master)](https://travis-ci.org/tiagocordeiro/django-divichild-builder)
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
