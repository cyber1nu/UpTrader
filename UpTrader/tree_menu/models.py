from django.db import models
""" For future I18N """
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('Имя'))
    parent = models.ForeignKey('self', default=None, on_delete=models.CASCADE, verbose_name=_('Родитель'),
                               null=True, blank=True)
    self_url = models.CharField(max_length=100, default='1', unique=True, verbose_name=_('Явная ссылка'))

    class Meta:
        verbose_name = _('Главная категория')
        verbose_name_plural = _('Главные категории')

    def __str__(self):
        return self.title

    def get_parent(self):
        if self.parent is not None:
            return self.parent.get_parent() + [self.parent.id, ]
        return []

    def get_children(self):
        return self.categorymodel_set.all()
