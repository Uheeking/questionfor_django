from django.utils import timezone
from django.shortcuts import render, redirect
from question.forms import QuestionForm
from django.views.decorators.csrf import csrf_exempt

from ..models import Question

@csrf_exempt
def createQuestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('question:index')
    else:
        form = QuestionForm()
    return render(request, 'question.html', {'form': form})
