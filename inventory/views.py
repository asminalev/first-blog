from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import *


class List(CreateView):
    model = Building
    fields = "__all__"
