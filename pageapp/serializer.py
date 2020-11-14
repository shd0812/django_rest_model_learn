#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/10 23:11
# @Author  cunfu
# @File serializer.py

from rest_framework import serializers
from pageapp import models


class SilkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Silk
        fields = '__all__'
        # fields = ["name"]

