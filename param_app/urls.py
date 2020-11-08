#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/8 10:51
# @Author  cunfu
# @File urls.py

from django.urls import path
from param_app import views

urlpatterns = [
    path('test/', views.ParamView.as_view()),
    path('roles/', views.RoleView.as_view()),
    path('userInfo/', views.UserInfoView.as_view()),


]