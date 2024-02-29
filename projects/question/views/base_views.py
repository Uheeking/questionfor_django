from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Q

from ..models import Question

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'question/profile.html', context)
