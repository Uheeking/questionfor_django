from django.contrib import admin
from django.urls import path, include
from question.views import base_views

urlpatterns = [
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('question/', include('question.urls')),
    path('common/', include('common.urls')),
]
