#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/1 21:57
# @Author  cunfu
# @File seriazalizer.py


from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Projects

class ProjectModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text='项目名称', label='项目名称', max_length=100,
                     validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目不可重名")])
    class Meta:
        model = Projects
        fields = "__all__"

