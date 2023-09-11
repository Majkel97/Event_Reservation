from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("management/", views.management, name="management"),
    path("delete/", views.delete, name="delete"),
]
