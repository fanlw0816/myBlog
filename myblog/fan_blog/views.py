from django.shortcuts import render
from .models import Category, Blog, Tag
from django.core.paginator import *

# Create your views here.


def index(request, pindex):
    if pindex == '':
        pindex = 1
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

    if bid == '':
        print(404)

    else:
        try:
            blog = Blog.objects.get(id=bid)
            context = {
                'blog': blog
            }
            return render(request, 'detail.html', context)
        except Exception as e:
            print(e)


def category(request, cid, pindex):
    if pindex == '':
        pindex = 1

    blogs = Category.objects.get(id=cid).blog_set.order_by("-created")
    categorys = Category.objects.all()
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'page': page,
        'categorys': categorys,
        'kind': "category/" + str(cid)
    }

    return render(request, 'index.html', context)


def tags(request, tid, pindex):
    if pindex == '':
        pindex = 1

    blogs = Tag.objects.get(id=tid).blog_set.order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'page': page,
        'kind': "tags/" + str(tid)
    }
    return render(request, 'tags.html', context)


def results(request, pindex):
    if pindex == '':
        pindex = 1

    keyword = request.GET["keyword"]
    blogs = Blog.objects.filter(title__icontains = keyword).order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'page': page,
        'kind': "results"
    }

    return render(request, 'search_result.html', context)


def profile(request):

    return render(request, 'profile.html')