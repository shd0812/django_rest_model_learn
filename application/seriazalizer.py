#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/10/30 23:24
# @Author  cunfu
# @File seriazalizer.py
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from application.models import Persons

SEX = (
    (1, "man"),
    (2, "woman")
)


# 自定义校验器
def is_validate_name(name):
    if name.endswith("王"):
        raise serializers.ValidationError("不能以王结尾")


class PersonsSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100,
                                 help_text="姓名",
                                 validators=[UniqueValidator(queryset=Persons.objects.all(), message="老王太多来"),
                                             is_validate_name],
                                 error_messages={"max_length":"name is too 长来"}) # 自定义错误提示
    # sex = serializers.IntegerField( help_text="性别", default="1", choices=SEX)
    phone = serializers.CharField(max_length=11, help_text="手机号",
                                  error_messages={"max_length": "手机好 is too 长来"}
                                  )
    address = serializers.CharField(max_length=200, help_text="家庭住址", allow_blank=True, allow_null=True)

    # 实例内单个字段校验
    def validate_name(self, value):
        if value.startswith("老"):
            raise serializers.ValidationError("不能以老开头")
        return value

    # 多个字段校验
    def validate(self, attrs):
        print(attrs)
        if attrs['phone'].startswith("135") or "井湾" in attrs['address']:
            raise serializers.ValidationError("电话不能以135开头，或者 地址不需要包含井")
        return attrs

    def create(self, validated_data):
        person = Persons.objects.create(**validated_data)
        return person

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.phone = validated_data['phone']
        instance.address = validated_data['address']
        instance.save()
        return instance

# 替代上面的手动生成属性的步骤，前提需要继承ModelSerializer
# 而且不需要手动写create 和update 实例方法
class PersonModelSerializer(serializers.ModelSerializer):
    # 如果需要自定义校验器，则需要覆盖自动生成的
    # name = serializers.CharField(max_length=100, help_text="姓名",
    #                              validators=[UniqueValidator(queryset=Persons.objects.all(), message="老王太多来"),
    #                                          is_validate_name])
    class Meta:
        # 1. 指定参考哪个模型类参考
        model = Persons
        # 2. 指定所有字段来生成序列化器
        fields = "__all__"
        # 3. 指定特定的字段生成序列化器
        # fields = ('id', 'name', 'phone')
        # 4. 排除某些不需要序列化的字段
        # exclude = ("sex", "address")
        # 5. 指定只读的字段
        # read_only_fields = ('name', )
        # 6. 指定字段错误信息
        # extra_kwargs = {
        #
        #     "address": {
        #         # "write_only": True,
        #         "error_message":
        #                     {"max_length": "地址不能太长"}
        #
        #                 }
        # }

    # 实例内单个字段校验
    def validate_name(self, value):
        if value.startswith("老"):
            raise serializers.ValidationError("不能以老开头")
        return value

    # 多个字段校验
    def validate(self, attrs):
        print(attrs)
        if attrs['phone'].startswith("135") or "井湾" in attrs['address']:
            raise serializers.ValidationError("电话不能以135开头，或者 地址不需要包含井")
        return attrs

