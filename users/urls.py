from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout_view, name="logout"),
]
