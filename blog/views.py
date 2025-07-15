from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from blog.forms import BlogForms, CommentForm
from blog.models import Blog, Like


@login_required
def home(request):
    blogs = Blog.objects.filter(published=True)
    search_published_blog = request.GET.get('search_published_blog')

    if search_published_blog:
        blogs = Blog.objects.filter(
            Q(title__icontains=search_published_blog) | Q(content__icontains=search_published_blog),
            published=True)

    context = {
        "blogs": blogs  # 'SELECT "blog_blog"."id", "blog_blog"."name" FROM "blog_blog"'
    }

    return render(request, 'blog/home.html', context=context)


@login_required
def home_out(request):
    blogs = Blog.objects.filter(published=False, author=request.user)
    search_published_blog = request.GET.get('search_unpublished_blog')

    if search_published_blog:
        blogs = Blog.objects.filter(
            Q(title__icontains=search_published_blog) | Q(content__icontains=search_published_blog),
            published=False, author=request.user)
    context = {
        "blogs": blogs  # 'SELECT "blog_blog"."id", "blog_blog"."name" FROM "blog_blog"'
    }

    return render(request, 'blog/home_out.html', context=context)


def create(request):
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
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
    comments = blog.comments.all()
    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect('detail', blog_id=blog.id)

    user_like = Like.objects.filter(user=request.user, blog=blog).first()
    if not user_like:
        user_like = Like.objects.create(user=request.user, blog=blog)
    context = {
        'blog': blog,
        "comments": comments,
        "comment_form": comment_form,
        "request_user_is_liked": user_like.is_liked,
        "user_likes_count": list(blog.likes.values_list('is_liked', flat=True)).count(True)
    }
    return render(request, 'blog/detail.html', context=context)


def like_dislike(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    user_like = Like.objects.filter(user=request.user, blog=blog).first()
    if not user_like:
        user_like = Like.objects.create(user=request.user, blog=blog)
    if user_like.is_liked:
        user_like.is_liked = False
    else:
        user_like.is_liked = True
    user_like.save()
    return redirect('detail', blog_id=blog_id)


def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
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
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    blog.delete()
    return redirect('home')

# lookup expr
# > 3  field__gt = 3
# >= 3  field__gte = 3

# < 3  field__lt = 3
# <= 3  field__lte = 3

# = 'text'  field__exact = 'text'
# = 'Text' or 'text'  field__iexact = 'text'

# = '23Text910'  field__contains = 'Text'
# = '23Text910' or 'asdatext4842'  field__icontains = 'Text'

# = 'Text910'  field__starstwith = 'Text'
# = 'Text910' or 'text4842'  field__istarstwith = 'Text'

# = '1389284Text'  field__endswith = 'Text'
# = '1389284Text' or '22313text'  field__iendswith = 'Text'

# field is null;   field__isnull=True
# field is not null;   field__isnull=False
