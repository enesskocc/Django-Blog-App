from django import forms
from .models import Post, Comment

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ('content',)
        exclude = ('user', 'post', 'author')