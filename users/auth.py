#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/7 18:40
# @Author  cunfu
# @File auth.py
from users.models import UserToken
from users.serializer import UserInfoSerializer, TokenSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import  AuthenticationFailed

class VipAuthTicate(BaseAuthentication):

    def authenticate(self, request):
        token = request._request.headers.get('token')
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed("认证失败")
        return (obj.user, obj)

    def authenticate_header(self, request):
        pass
