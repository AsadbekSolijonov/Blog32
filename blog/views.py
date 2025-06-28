from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import BlogForms
from blog.models import Blog


def home(request):
    context = {
        "blogs": Blog.objects.filter(published=True)  # 'SELECT "blog_blog"."id", "blog_blog"."name" FROM "blog_blog"'
    }

    return render(request, 'blog/home.html', context=context)


def home_out(request):
    context = {
        "blogs": Blog.objects.filter(published=False)  # 'SELECT "blog_blog"."id", "blog_blog"."name" FROM "blog_blog"'
    }

    return render(request, 'blog/home_out.html', context=context)


def create(request):
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            if blog.published:
                return redirect('home')
            return redirect('home_out')
    else:
        form = BlogForms()
    context = {
        'form': form
    }
    return render(request, 'blog/create.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context=context)


def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            if blog.published:
                return redirect('home')
            return redirect('home_out')
    else:
        form = BlogForms(instance=blog)
    return render(request, 'blog/update.html', {'form': form, 'blog': blog})


def delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('home')
