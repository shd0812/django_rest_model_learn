#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/1 21:24
# @Author  cunfu
# @File urls.py


from django.urls import path
from projects import views


urlpatterns = [
    path('projects', views.ProjectView.as_view()),
    path('projects/<int:id>', views.ProjectsDetail.as_view())
]