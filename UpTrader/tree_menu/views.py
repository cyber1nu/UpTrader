from django.shortcuts import render
from django.views import generic, View
from .models import CategoryModel
from django.core.exceptions import ObjectDoesNotExist


class IndexDetailView(generic.DetailView):
    template_name = 'base.html'
    model = CategoryModel

    def get_context_data(self, *args, **kwargs):
        context = super(IndexDetailView, self).get_context_data(*args, **kwargs)
        context['firsts'] = CategoryModel.objects.filter(parent=None)
        context['object'] = kwargs['object']
        return context


def fill_db():
    data = (
            (None, 'Бытовая химия'),
            (None, 'Продукты'),
            ('Бытовая химия', 'Моющие средства'),
            ('Бытовая химия', 'Средства гигиены'),
            ('Бытовая химия', 'Средства для ванны'),
            ('Бытовая химия', 'Средства для мытья полов'),
            ('Продукты', 'Пирожные'),
            ('Продукты', 'Мясные изделия'),
            ('Продукты', 'Напитки'),
            ('Продукты', 'Булочные изделия'),
            ('Моющие средства', 'Пемолюкс'),
            ('Средства гигиены', 'Мыло снежинка'),
            ('Средства для ванны', 'Тайд'),
            ('Средства для мытья полов', 'Лысый из бразерс'),
            ('Пирожные', 'Картошка'),
            ('Мясные изделия','Стейк'),
            ('Напитки', 'Добрый Кола'),
            ('Булочные изделия', 'Самса с сыром'),
            )

    for item in data:
        try:
            parent = CategoryModel.objects.get(title=item[0])
        except ObjectDoesNotExist:
            parent = None

        CategoryModel.objects.create(
            title=item[1],
            parent=parent
        )

    return
