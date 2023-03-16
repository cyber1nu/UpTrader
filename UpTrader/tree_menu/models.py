from django.db import models
from django.urls import reverse
""" For future I18N """
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('Имя'))
    parent = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, verbose_name=_('Родитель'),
                               null=True, blank=True)

    class Meta:
        verbose_name = _('Главная категория')
        verbose_name_plural = _('Главные категории')

    def __str__(self):
        return self.title

    def get_parent(self):
        if self.parent:
            return self.parent.get_parent() + [self.parent.id, ]
        return []

    def get_absolute_url(self):
        return reverse('tree_menu_tree', args=[self.id])
