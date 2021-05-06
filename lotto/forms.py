from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    # form을 통해 받을 메타 데이터 (DB 테이블 연결)
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text')
