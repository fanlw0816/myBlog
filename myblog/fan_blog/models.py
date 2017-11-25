from django.db import models
from DjangoUeditor.models import UEditorField


class Category(models.Model):
    name = models.CharField('名称', max_length=16)
    isDelete = models.BooleanField('逻辑删除', default=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', max_length=16)
    isDelete = models.BooleanField('逻辑删除', default=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    isDelete = models.BooleanField('逻辑删除', default=False)
    intro = UEditorField('简介', width=600, height=300, default='', toolbars='full')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    click = models.IntegerField(default=0)

    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    content = UEditorField('内容', height=500, width=1200,
                 default='', blank=True, imagePath="images/",
                 toolbars='full', filePath='files/')

    def __str__(self):
        return self.title


class Comment(models.Model):

    blog = models.ForeignKey(Blog, verbose_name='博客')
    isDelete = models.BooleanField('逻辑删除', default=False)
    head_img = models.ImageField(upload_to='images/', default='images/head_img.png')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱', default='')
    link = models.CharField('链接', max_length=30, default='')
    content = models.CharField('内容', max_length=200)
    created = models.DateTimeField('发布时间', auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name


class Browse(models.Model):

    number = models.IntegerField(default=0)
