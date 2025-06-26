from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def home(request):
    context = {
        "blogs": Blog.objects.all()  # 'SELECT "blog_blog"."id", "blog_blog"."name" FROM "blog_blog"'
    }

    return render(request, 'blog/home.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context=context)
