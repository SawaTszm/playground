# tutorial-django

reference: [Writing your first Django app, part 1 | Django documentation | Django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)  

## First Django app

### Make project

```bash
$django-admin startproject <project-name>
```

`django-admin` is able to change to `python -m django`.  
Read later: [django-admin and manage.py | Django documentation | Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/)  

### Development server

```bash
cd <project-name>
python manage.py runserver
```

It started the Django development server, let's visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with Web brouser.  
If you want to change the port and IP, use: `$python manage.py runserver 0:8080` (0 is mean `0.0.0.0`)  
reference: [django-admin and manage.py | Django documentation | Django](https://docs.djangoproject.com/en/3.2/ref/django-admin/#django-admin-runserver)  

![スクリーンショット 2021-05-18 20 51 02](https://user-images.githubusercontent.com/48425020/118646356-102dd900-b81b-11eb-8137-18cf0faae608.png)

So cute :)  

And the development server automatically reloads, don't need to restart server each and every. But some actions (like adding files) don't trigger a restart.  

### Creating the Polls app

Django has a function that automatically generates the basic directory structure, so can focus on writing code.  
(TIPS: The app is able to exist multiple in a project. Also the app is able to exist in multiple projects.)  

use:

```bash
$python manage.py startapp polls
```

It created `polls` directory. this directory structure will house the poll application.  

### Write first view

Let's open the file `polls/view.py` and write following code:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

This is the most simplest View of Django.  
It needs to relation URL for calling view. To do so, it need URLconf. Let's create file `polls/urls.py` and write following code:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Next step is taking effect `polls.urls` for root (URLconf). Let's Add the import `django.urls.include` to `mysite/urls.py` and insert `include()` into the list of `urlpatterns`. Then it woll look like this:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

`include()` is able to refer to other URLconf. When Django encounters `include()`, it cut URL that part matched that time and pass remain URL to URLconf (`include()` URLconf) for next process.  
Read later: [Writing your first Django app, part 1 | Django documentation | Django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#write-your-first-view)  

Let's visit [http://localhost:8000/polls/](http://localhost:8000/polls/). This is defined by view index.

`path()` receives 4 arguments. `route` and `view` is requirement, `kwargs` and `name` is optional.  

#### path() arguments: route

`route` is string include URL pattern. When Django process request, it start from top of `urlpatterns`, and check its list by order. It continues until find requested URL.  

The pattern doesn't search parameter of GET or POST and domain.  

Example:  
Request to `https://www.example.com/myapp/`, URLconf looks `myapp/`.  
Request to `https://www.example.com/myapp/?page=3`, URLconf also looks `myapp/`.  

#### path() arguments: view

When Django finds a matching pattern, it calls requested view function. In this case, `HttpRequest` object is first argument, and captured values from the route is keyword arguments.

#### path() arguments: kwargs

It can pass optional keyword arguments to view function.  
(This argument is not used this tutorial)

#### path() arguments: name

If naming URL, can refer from anywhere Django. Specially taking effect in template. Because of this convenient function, can change only one file when need to update URL of project.  

### Setting Database

Let's open file `mysite/settings.py`. This one is usual python module that has values of module level to express Django settings.  

By default, use SQLite. (This is the most easiest way)  Because SQLite is included in Python first.  
However, if want to use project in production, it's better to use scalable DB like PostgresSQL because avoid to transition DB as your headache.  

This tutorial (mean this repository) will use SQLite,  
Read later: [Writing your first Django app, part 2 | Django documentation | Django](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#database-setup)

When change `mysite/settings.py`, add your timezone to `TIME_ZONE`.  

Also, caution `INSTALLED_APPS` in first line of the file . This one has all names of Django app that be able in this Django instance.  

By default, `INSTALLED_APPS` has following apps:  

* django.contrib.admin
* django.contrib.auth
* django.contrib.contenttypes
* django.contrib.sessions
* django.contrib.messages
* django.contrib.staticfiles

these apps need database, let's create it.  
Use:

```bash
$python manage.py migrate
```

`migrate` command refers settings of `INSTALLED_APPS`, and create all database table following the file `mysite/settings.py`.  This database migration is distributed with app.  

TIPS: If you don't need default `INSTALLED_APPS`, can remove choiced line, before use `migrate` command. this command executes for the sake of only apps included `INSTALLED_APPS`.  

### Still do from here

I'm out of energy for translate hehe  
(now I try to read document (Language:ja) and translate it English by oneself for my study)  
I'll continue again soon.

NEXT: [Writing your first Django app, part 2 | Django documentation | Django](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#creating-models)