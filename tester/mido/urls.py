from django.urls import path
from mido import views

urlpatterns = [
    path('', views.didi, name='n1'),
    path('contactus', views.contact, name='c1'),
    path('aboutus', views.about, name='a1'),

]
