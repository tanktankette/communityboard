from django import forms
from .models import Post, Board
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    text = forms.Textarea()
    author = forms.CharField(required=False)

    class Meta:
        model = Post
        fields = ('text', 'author')
