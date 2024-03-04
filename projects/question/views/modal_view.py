from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
