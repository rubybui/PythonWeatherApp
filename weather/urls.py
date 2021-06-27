from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
# if we open URL 127.0.0.1:8000 it will run a function called “index” in the views.py file.

