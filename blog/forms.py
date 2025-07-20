from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget

from blog.models import Blog, Comment
from django import forms


class BlogForms(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'type', 'photo', 'published')
        widgets = {
            'content': CKEditor5Widget(attrs={"class": 'django_ckeditor_5'}, config_name="extends")
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False


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
