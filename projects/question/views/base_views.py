from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Q

from ..models import Question

def index(request):
    # page = request.GET.get('page', '1')  # 페이지
    # context = {'question_list': page_obj, 'custom_range':custom_range, 'max_index': max_index, 'page': page, 'kw': kw}
    return HttpResponse("안녕하세요 question 오신것을 환영합니다.")
