from django.urls import path
from . import views

#URLConf
urlspatterns = [
    path('hello', views.say_hello)
]