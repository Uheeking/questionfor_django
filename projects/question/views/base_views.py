from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Q

from ..models import Question

def index(request):
    Uheeking = 'Uheeking'
    # page = request.GET.get('page', '1')  # 페이지
    context = { 'Uheeking':Uheeking}
    return render(request, 'question/profile.html', context)
