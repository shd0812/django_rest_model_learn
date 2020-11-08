#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/7 16:08
# @Author  cunfu
# @File urls.py

from django.urls import path, re_path
from users import views


urlpatterns = [
    path('info/', views.UserInfoView.as_view()),
    path('userOrder/', views.OrderView.as_view()),

    # path('userList/', views.UserView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/userList/$', views.UserView.as_view()),

    # path('projects/<int:id>', views.ProjectsDetail.as_view())
]