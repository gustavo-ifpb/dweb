# Django

1. Criar ambiente virtual e habilitar o ambiente virtual

```shell
$ python3 -m venv env
$ source env/bin/activate
```

2. Instalar o django

```shell
$ pip install django
```

3. Criar um projeto django

```shell
$ django-admin startproject movies
```

4. Criar a pasta app e criar a aplicação movie

```shell
$ mkdir app
$ cd app
$ python ../manage.py startapp movie
```