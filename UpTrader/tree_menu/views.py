from django.shortcuts import render
from django.views import generic, View
from .models import CategoryModel
from django.views.generic.edit import FormMixin
from .forms import MenuForm


def index(request, pk=None):
    context = {'request': request}
    return render(request, 'list.html', context)
