from django.shortcuts import render
from .models import Category, Blog, Tag
from django.core.paginator import *

# Create your views here.


def index(request):
    pindex = int(request.GET.get('page', 1))
    blogs = Blog.objects.order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)

    categorys = Category.objects.all()
    context = {
        'page': page,
        'categorys': categorys,
        'kind': 'index'
    }

    return render(request, 'index.html', context)


def details(request, bid):
    blog = Blog.objects.get(id=bid)
    blog.click += 1
    blog.save()
    context = {
        'blog': blog
    }
    return render(request, 'detail.html', context)


def category(request, cid):
    pindex = int(request.GET.get('page', 1))
    blogs = Category.objects.get(id=cid).blog_set.order_by("-created")
    categorys = Category.objects.all()
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'cid': int(cid),
        'page': page,
        'categorys': categorys,
        'kind': "category/" + str(cid)
    }

    return render(request, 'index.html', context)


def tags(request, tid):
    pindex = int(request.GET.get('page', 1))
    tag = Tag.objects.get(id=tid)
    blogs = tag.blog_set.order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'result': tag.name,
        'page': page,
        'kind': "tags/" + str(tid)
    }
    return render(request, 'search_result.html', context)


def results(request):
    pindex = int(request.GET.get('page', 1))

    keyword = request.GET["keyword"]
    blogs = Blog.objects.filter(title__icontains = keyword).order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'result': keyword,
        'page': page,
        'kind': "results"
    }

    return render(request, 'search_result.html', context)


def profile(request):

    return render(request, 'profile.html')