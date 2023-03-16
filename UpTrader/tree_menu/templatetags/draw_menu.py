from django import template
from django.shortcuts import get_object_or_404
from tree_menu.models import CategoryModel
from django.core.exceptions import ObjectDoesNotExist


register = template.Library()


@register.inclusion_tag('list.html', takes_context=True)
def draw(context, name):
    category = get_object_or_404(CategoryModel, title=name)
    parent_ids = category.get_parent()
    context['parents'] = []
    for par in parent_ids:
        context['parents'].append(CategoryModel.objects.get(id=par))
    context['children'] = CategoryModel.objects.filter(parent=category.id)
    return context

