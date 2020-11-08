#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/1 21:24
# @Author  cunfu
# @File urls.py


from django.urls import path
from projects import views


urlpatterns = [
    path('pp/', views.ProjectView.as_view()),
    path('pp/<int:id>', views.ProjectsDetail.as_view())
]