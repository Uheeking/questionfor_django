from django.urls import path

from .views import base_views, question_views

app_name = 'question'

urlpatterns = [
    path('', base_views.index, name='index'),
    
    path('question/create/',
         question_views.createQuestion, name='question_create'),
    path('question/delete/<int:question_id>/',
         question_views.deleteQuestion, name='question_delete'),
]
