from django import forms
from .models import Blog,Comment
from django.forms import ModelForm

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label="comment"

