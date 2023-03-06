from django import forms
from .models import CategoryModel


class MenuForm(forms.ModelForm):

    class Meta:
        model = CategoryModel
        fields = ('title', )
