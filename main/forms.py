from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Title',
            'content': 'Content',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        labels = {
            'author': 'Name',
            'text': 'Comment',
        }
