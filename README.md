# 版本
- mysql ==5.7.19-0ubuntu0.16.04.1 
- django ==1.11.3
- PyMySQL ==0.7.11
- mysqlclient ==1.3.10
- python ==3.5.2
- uwsgi ==2.0.15
- celery-with-redis ==3.0
- django-celery-results ==1.0.1
- celery ==4.1.0
- DjangoUeditor ==1.8.143(python3需要手动下载 https://github.com/twz915/DjangoUeditor3)

# 历史
#### 2017-11
celery遇到一个版本的坑，以前开发用的 django-celery 在 django 1.8 之后的版本用不了，我直接使用的celery 4.1.0, 根据官方文档配置成功，[celery官方文档](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

#### 2017-8

- create a blog program  
---

# TODO
- [x] ~~站点浏览量统计~~
- [x] ~~blog评论功能~~
- [x] ~~celery异步处理邮件~~
- [ ] 站内搜索功能
- [ ] 邮件推送  

---



