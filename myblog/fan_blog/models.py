from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Category(models.Model):
    """
    分类
    """

    name = models.CharField('名称', max_length=16)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签
    """

    name = models.CharField('名称', max_length=16)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """

    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = UEditorField('内容', height=500, width=1200,
                 default='', blank=True, imagePath="images/",
                 toolbars='full', filePath='files/')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """

    blog = models.ForeignKey(Blog, verbose_name='博客')

    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)

    created = models.DateTimeField('发布时间', auto_now_add=True)