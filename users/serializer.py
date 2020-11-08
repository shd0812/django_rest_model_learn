#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/7 17:01
# @Author  cunfu
# @File serializer.py
from rest_framework import serializers
from users.models import  UserInfo, UserToken
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = "__all__"

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'

    def create(self, validated_data):
        UserToken.objects.update_or_create(user=obj, defaults={"token": token})

