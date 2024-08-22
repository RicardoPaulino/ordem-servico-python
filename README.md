# Ordem de Serviço (Django)
<p>Projeto de order de serviço utilizando Django</p>

### Packages

### Passo a Passo
#### 1 . Criar ambiente virtual
> python3 -m venv .venv 

> source .venv/bin/activate

#### 2 . Install Django

> pip install django django-extensions python-decouple

> pip install django-ninja

#### 3 . Criar arquivo requirements.txt

> pip freeze

> pip freeze > requirements.txt

#### 4 . Gerar arquivo .env randomico

```
"""
Python SECRET_KEY generator.
"""
import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()"
size = 50
secret_key = "".join(random.sample(chars, size))

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%_"
size = 20
password = "".join(random.sample(chars, size))

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1,.localhost,0.0.0.0

#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#POSTGRES_DB=
#POSTGRES_USER=
#POSTGRES_PASSWORD=%s
#DB_HOST=localhost

#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=localhost
#EMAIL_PORT=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
#EMAIL_USE_TLS=True
""".strip() % (secret_key, password)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')

```

<h5>Executar o comando para gerar o arquivo .env</h5>

> python contrib/env_gen.py

#### 5 . Criar o projeto django 

> django-admin startproject backend .

> python ../manage.py startapp core