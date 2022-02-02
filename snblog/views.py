from django.shortcuts import render, get_object_or_404
from snblog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


def about_me(request):
    return render(request, "snblog/about_me.html")


def startpage(request):
    return render(request, "snblog/startpage.html")


def posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts.order_by("-id"), 5)

    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request, "snblog/post_list.html", {"posts": posts, "page": page})


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment.filter(active=True)
    form = CommentForm


    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

    return render(request, "snblog/post_detail.html", {"post": post,
                                                       "comments": comments,
                                                       "form": form
                                                       })
