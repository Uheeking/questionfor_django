from django import forms
from question.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        
        labels = {
            'subject': '제목',
            'content': '내용',
        }