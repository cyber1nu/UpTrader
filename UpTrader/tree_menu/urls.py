from django.urls import path
from .views import index


urlpatterns = [
    path('', index, name='tree_menu'),
    path('<int:pk>', index, name='tree_menu_tree')
]
