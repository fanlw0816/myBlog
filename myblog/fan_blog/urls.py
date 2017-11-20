from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog/(\d+)/', views.details),
    url(r'^category/(\d+)/$', views.category),
    url(r'^index/$', views.index),
    url(r'^tags/(\d+)/$', views.tags),
    url(r'^get_tags/$', views.get_tags),
    url(r'^get_hot/$', views.get_hot),
    url(r'^results/$', views.results),
    url(r'^profile/$', views.profile),
    url(r'^visitor_number/$', views.visitor_number),
]
