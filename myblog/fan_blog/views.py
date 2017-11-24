from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponse
from .models import *
from django.core.paginator import *
from PIL import Image, ImageDraw, ImageFont
import string, random

# Create your views here.


def index(request):
    pindex = int(request.GET.get('page', 1))
    blogs = Blog.objects.filter(isDelete=False).order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)

    categorys = get_category()
    # tags_show = Tag.objects.all()
    context = {
        'page': page,
        'categorys': categorys,
        # 'tags': tags_show,
        'kind': 'index'
    }

    return render(request, 'index.html', context)


def get_category():
    categorys = Category.objects.filter(isDelete=False)
    category_list = []
    for cate in categorys:
        cate_one = {}
        cate_one['name'] = cate.name
        cate_one['id'] = cate.id
        cate_one['count'] = cate.blog_set.filter(isDelete=False).count()
        category_list.append(cate_one)

    return category_list


def details(request, bid):
    try:
        blog = Blog.objects.get(id=bid, isDelete=False)
    except:
        raise Http404


    blogs = blog.category.blog_set.filter(isDelete=False).order_by('id')
    blog_index = list(blogs).index(blog)
    lenght = len(blogs)
    prev_index = blog_index - 1
    next_index = blog_index + 1

    if prev_index < 0:
        prev_blog = None
    else:
        prev_blog = blogs[prev_index]

    if next_index >= lenght:
        next_blog = None

    else:
        next_blog = blogs[next_index]

    context = {
        'blog': blog,
        'prev_blog': prev_blog,
        'next_blog': next_blog
    }
    response = render(request, 'detail.html', context)
    article_flags = request.COOKIES.get('article_flags', '')
    flag_list = article_flags.split('==')
    if bid not in flag_list:
        blog.click += 1
        blog.save()
        flag_list.append(bid)
        response.set_cookie('article_flags', '=='.join(flag_list), expires=60*60*24*7)

    return response


def category(request, cid):
    try:
        blogs = Category.objects.get(id=cid, isDelete=False).blog_set.filter(isDelete=False).order_by("-created")
    except:
        raise Http404

    pindex = int(request.GET.get('page', 1))
    categorys = get_category()
    # tags_show = Tag.objects.all()
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'cid': int(cid),
        'page': page,
        'categorys': categorys,
        # 'tags': tags_show,
        'kind': "category/" + str(cid)
    }

    return render(request, 'index.html', context)


def tags(request, tid):
    try:
        tag = Tag.objects.get(id=tid, isDelete=False)
    except:
        raise Http404

    pindex = int(request.GET.get('page', 1))
    blogs = tag.blog_set.filter(isDelete=False).order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'result': tag.name,
        'page': page,
        'kind': "tags/" + str(tid)
    }
    return render(request, 'search_result.html', context)


def get_tags(request):
    tags_show = Tag.objects.filter(isDelete=False)
    datas = []
    for tag in tags_show:
        info = {}
        info['id'] = tag.id
        info['name'] = tag.name
        datas.append(info)

    return JsonResponse({"datas": datas})


def get_hot(request):
    blogs = Blog.objects.filter(isDelete=False).order_by('-click')[:6]
    datas = []
    for blog in blogs:
        info = {}
        info['id'] = blog.id
        info['title'] = blog.title
        datas.append(info)

    return JsonResponse({"datas": datas})


def results(request):
    pindex = int(request.GET.get('page', 1))

    keyword = request.GET["keyword"]
    blogs = Blog.objects.filter(title__icontains=keyword, isDelete=False).order_by("-created")
    paginator = Paginator(blogs, 3)
    page = paginator.page(pindex)
    context = {
        'result': keyword,
        'page': page,
        'kind': "results",
        'keyword': '&keyword=%s' % keyword
    }

    return render(request, 'search_result.html', context)


def profile(request):

    return render(request, 'profile.html')

def visitor_number(request):
    brose = Browse.objects.all()[0]
    return JsonResponse({'number': brose.number})

def captcha(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    # 内存文件操作(python3)
    from io import BytesIO
    buf = BytesIO()

    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')