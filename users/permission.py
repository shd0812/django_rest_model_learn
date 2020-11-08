#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/7 19:16
# @Author  cunfu
# @File permission.py
from rest_framework.permissions import BasePermission


# 权限校验
class myPermission(BasePermission):

    def has_permission(self, request, view):
        print(request.user.userType)
        print(type(request.user.userType))
        if request.user.userType == '3':
            return True
