from django.forms import ModelForm
from blog.models import Blog


class BlogForms(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ('author', )
