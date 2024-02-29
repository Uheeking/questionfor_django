from django.urls import path

from .views import base_views, modal_view

app_name = 'question'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('modal/',
         modal_view.createQuestion, name='modal'),
]
