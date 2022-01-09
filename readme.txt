install python  // add it to path variable during intallination  using software 
pip install virtualenv    >> install virtual environment 
python -m venv env        >> create virtual environment named env
env\Scripts\activate     >>acivate virtual environment
deactivate               >>deacivate virtual environment


env\Scripts\activate
install python specific version  and  django specific version in virtual environment
python --version          >>check python version
django-admin --version    >>check django version
pip freeze                >>tells us python & django version and related libraries installed in virtal environment 


django-admin startproject tester    >>create project tester
cd tester
python manage.py runserver
python manage.py startapp mido 
after that add mido in installed apps of settings file of tester folder INSTALLED_APPS = ['mido','django.contrib.admin',]
and create urls.py in mido folder

In tester.urls
add include >>>        from django.urls import path,include
add         >>>        path('mido/', include('mido.urls'))

In mido ->urls.py
from mido import views
path('', views.didi, name='n1'),
path('contactus', views.contact, name='c1'),
path('aboutus', views.about, name='a1'),

In mido ->views.py
from django.shortcuts import render

def didi(request):
    content = {'fruit': 'honey'  }
    return render(request,'hi.html', content)

def about(request):
    content = { 'fruit': 'apple'}
    return render(request,'about.html', content)

def contact(request):
    content = {'fruit': 'carrot' }
    return render(request,'contact.html', content)




create templates directory in mido directory and add hi.html , about.html , contact.html
whole hi.html file content
{% extends 'base.html' %}

{% block title %}
<h1>Home Page</h1>
{% endblock title %}

{% block ginga %}
<h1>{{fruit}} </h1>
{% endblock ginga %}




-------------------------------------
whole about.html file content
{% extends 'base.html' %}

{% block title %}
<h1>About Us page </h1>
{% endblock title %}

{% block ginga %}
<h1>{{fruit}} </h1>
{% endblock ginga %}



-----------------------------------
whole contact.html fille content
{% extends 'base.html' %}

{% block title %}
<h1>Contact Us page</h1>
{% endblock title %}

{% block ginga %}
<h1>{{fruit}} </h1>
{% endblock ginga %}







Create templates folder in tester directory  and add base.html
in settings.py of tester add  'DIRS': [BASE_DIR / "templates",],
like TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates",],
        'APP_DIRS': True,
}
]







create static folder in tester directory and add css,js,image director. add logo.png in image directory.
add in setting file of tester directory          STATICFILES_DIRS = [BASE_DIR / "static"]
like 
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

add in base.html file ,following lines:
{% load static %}
<img src="{% static "image/logo.png" %}">








whole base.html file content
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<img src="{% static "image/logo.png" %}">
<nav style="display: flex; justify-content:space-evenly;">
    <a href="{% url 'n1' %}">Home</a>
    <a href="{% url 'a1' %}">About Us</a>
    <a href="{% url 'c1' %}">Contact</a>
</nav>

{% block title %}
{% endblock title %}

{% block ginga %}
{% endblock ginga %}

</body>
</html>

