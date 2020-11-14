#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/10 23:00
# @Author  cunfu
# @File urls.py



from django.urls import path, re_path, include
from rest_framework import routers
from pageapp import views


route = routers.SimpleRouter()
route.register(r'inter',views.ModelView)


urlpatterns = [
    path('list/', views.PageView.as_view()),
    path('model/', views.ModelView.as_view({'get': 'list', 'post': "create"})),
    path('model/names/', views.ModelView.as_view({'get': 'names'})),
    # re_path('model/(?P<pk>\d+)/$', views.ModelView.as_view({'get': 'retrieve', "delete": "destroy",  'put': "update", "patch": "partial_update", })),
    path('model/<int:pk>/', views.ModelView.as_view({'get': 'retrieve', "delete": "destroy",  'put': "update", "patch": "partial_update", })),
    path('phones/', views.PhoneView.as_view()),
    path("", include(route.urls))
]