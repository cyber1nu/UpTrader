from django import template
from django.shortcuts import get_object_or_404
from tree_menu.models import CategoryModel
from django.core.exceptions import ObjectDoesNotExist


register = template.Library()


@register.inclusion_tag('list.html', takes_context=True)
def draw_menu(context, category):
    category = get_object_or_404(CategoryModel, title=category, parent=None)
    temp_context = {'category': category}
    pk = category.parent
    try:
        if pk is None:
            temp_context['parent_ids'] = []
            return temp_context
        active_category = CategoryModel.objects.get(self_url=pk)
        print(active_category.parent)
    except ObjectDoesNotExist:
        pass
    else:
        parent_ids = active_category.get_parents() + [active_category.id, ]
        temp_context['parent_ids'] = parent_ids
    return temp_context


@register.inclusion_tag('list.html', takes_context=True)
def draw_menu_children(context, category_id):
    category = get_object_or_404(CategoryModel, pk=category_id)
    temp_context = {'category': category}
    if 'parent_ids' in context:
        temp_context['parent_ids'] = context['parent_ids']
    return temp_context
