# coding:utf-8
__author__ = 'Haddy Yang(Ysh)'
__start_date__ = '2016-06-12'
"""
    likes app
"""
from django.conf.urls import include, url
from . import views

# http://localhost:8000/likes/ +
# 在project的urls.py导入整个url配置
urlpatterns = [
    url(r'^likes_change/$', views.likes_change, name='likes_change'),
    url(r'^likes_nums/$', views.likes_nums, name='likes_nums'),
]