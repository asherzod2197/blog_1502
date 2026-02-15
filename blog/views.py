from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.views.decorators.http import require_POST


def index(request):
    posts = Post.published.all()
    context = {
        'posts': posts[:6],
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def single(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context= {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'single.html', context=context)


@require_POST
def post_comment(request, id):
    post = get_object_or_404(Post,
        id=id,
        status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    context = {
        'post': post,
        'form': form,
        'comment': comment,
        'comments': post.comments.filter(active=True)
    }

    return render(request, 'single.html', context=context)