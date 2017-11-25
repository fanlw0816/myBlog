from __future__ import absolute_import, unicode_literals
from fan_blog.models import Blog
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_comment_mail(nickname, email, link, blog_id, comment):
    print('开始发送！')
    blog = Blog.objects.get(id=blog_id)
    msg = '<div><div><p>昵称：%s</p>\
            <p>邮箱：%s</p>\
            <p>链接：%s</p>\
            <p>来自博客：<a href="http://fanliwei.top/blog/%s/">%s</p>\
            </div><p>评论内容：%s</p></div>' % (nickname, email, link, blog_id, blog.title, comment)

    send_mail('来自 (%s) 的blog评论' % nickname, '', settings.EMAIL_FROM, [settings.EMAIL_MYSELF], html_message=msg)
    print('结束！')