from django.urls import path
from .views import IndexDetailView


urlpatterns = [
    path('trader/<int:pk>/', IndexDetailView.as_view(), name='tree_menu_tree')
]
