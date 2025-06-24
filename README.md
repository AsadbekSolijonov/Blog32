# Blog32

Tavsif: Mening Brinichi Django Blogim

# Loyiha uchun papka yaratish:

```$ mkdir project_name```

```$ cd project_name```

# Virtual Enivironment yaratish

```$ python -m venv .venv```

-Windowds:
```$ cd .venv/Scripts/activate```

-MacOS:
```$ source .venv/bin/activate```

# Installation

```$ pip install django```

# Configration fayl yaratish:

```$ django-admin startproject config .```

# Loyihani ishga tushirish:

```$ python manage.py runserver```

# Django App yaratish:

```$ python manage.py startapp blog```

- Har doim ```app``` yaratilgadan keyin ro'yxatdan o'zgazing:

- [X] 👉 ```/config/settings.py```

<pre>
INSTALLED_APPS = [
    # ...,
    'blog',
]
</pre>

# Migrations

```
$ python manage.py migrate
```

# Superuser yaratish

```$ python manage.py createsuperuser```

<pre>
Username (leave blank to use 'asadbeksolijonov'): admin
Email address: example@gmail.com
Password: ***
Password (again): ***
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
</pre>

# Loyihani ishga tushirish:

```$ python manage.py runserver```



# Eslatma:
**Agar Modelda(```models.py```) nimadur o'zgarish bo'lsa**

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```