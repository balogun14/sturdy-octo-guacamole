from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator,EmptyPage
# Create your views here.
from .models import Post


def post_list(request):
    """
    docstring
    """
    post_list = Post.published.all()
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "list.html", {"posts": posts})


def post_detail(request,year,month,day,post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found")
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month = month,
        publish__day = day,
    )

    return render(request, "detail.html", {"post": post})
