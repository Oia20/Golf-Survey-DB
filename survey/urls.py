from django.urls import path
from . import views

urlpatterns = [
    path("", views.golfsurv, name="index"),
]