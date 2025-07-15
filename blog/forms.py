from django.forms import ModelForm
from blog.models import Blog, Comment
from django import forms


class BlogForms(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ('author',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        labels = {
            'message': ''
        }
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write a message...'
            }),
        }
