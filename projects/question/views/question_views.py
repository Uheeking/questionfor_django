from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from question.forms import QuestionForm
from django.views.decorators.csrf import csrf_exempt

from ..models import Question

@csrf_exempt
@login_required(login_url='common:login')
def createQuestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('question:index')
    else:
        form = QuestionForm()
    return render(request, 'question.html', {'form': form})

@login_required(login_url='common:login')
def deleteQuestion(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('question:index')
    messages.success(request, '삭제되었습니다.')
    # question.delete()
    return redirect('question:index')