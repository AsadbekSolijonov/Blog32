from django.shortcuts import render
from random import randint
from blog.models import Blog


def home(request):
    a = randint(1, 100)
    b = randint(1000, 10000)
    c = a + b

    context = {
        "a": a,
        "b": b,
        "c": c,
        "blogs": Blog.objects.all()  # 'SELECT "blog_blog"."id", "blog_blog"."name" FROM "blog_blog"'
    }

    return render(request, 'base.html', context=context)
