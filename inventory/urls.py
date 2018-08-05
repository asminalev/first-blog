from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.List.as_view()),
]