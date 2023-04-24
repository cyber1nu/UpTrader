from django.shortcuts import render
from django.views import generic, View
from .models import CategoryModel



class IndexDetailView(generic.DetailView):
    template_name = 'base.html'
    model = CategoryModel

    def get_context_data(self, *args, **kwargs):
        context = super(IndexDetailView, self).get_context_data(*args, **kwargs)
        context['firsts'] = CategoryModel.objects.filter(parent=None)
        context['object'] = kwargs['object']
        return context


