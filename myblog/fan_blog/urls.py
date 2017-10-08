from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^()$', views.index),
    url(r'^blog/(\d+)', views.details),
    url(r'^category/(\d+)/(\d*)$', views.category),
    url(r'^index/(\d+)$', views.index),
    url(r'^tags/(\d+)/(\d*)$', views.tags),
    url(r'^results/(\d*)$', views.results),
    url(r'^profile$', views.profile),
]
