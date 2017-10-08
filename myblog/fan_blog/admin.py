from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created', 'category']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'name', 'email', 'content', 'created']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
