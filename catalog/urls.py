# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.product_list,name='product_list'),
	url(r'^([\w_-]+)/$', views.category, name='category'),
]