from django.shortcuts import render, get_object_or_404
from snblog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    return render(request, "snblog/post_detail.html", {"post": post})

