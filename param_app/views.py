from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from param_app.models import  Role, UserInfo
from rest_framework import serializers

# Create your views here.
class ParamView(APIView):
    parser_classes = [JSONParser, ]
    def get(self, request):
        return HttpResponse("hello world")

    def post(self, request):


        print(request.body)
        print(request.data)
        print(request.body)
        print(type(request.data))
        print(type(request.body))
        return HttpResponse("i am post")


class RoleSerializer(serializers.ModelSerializer):
    username = serializers.CharField
    class Meta:
        model = Role
        # fields
        fields = "__all__"

class RoleView(APIView):
    def get(self, request):
        obj = Role.objects.all()
        res = RoleSerializer(obj, many=True)

        return JsonResponse(res.data, safe=False)


# class UserInforSerializer(serializers.Serializer):
#     userName = serializers.CharField()
#     password = serializers.CharField()
#     # pd = serializers.CharField(source="password")
#     Type = serializers.CharField(source="get_user_type_display")
#     gp = serializers.CharField(source='group.title')
#     role = serializers.SerializerMethodField()
#     def get_role(self, row):
#
#         return [{"id": item.id, "title": item.title} for item in  row.role.all()]


class UserInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        depth = 1 # 不要超过3    对着depth增多，返回关联表的层级越多
        # fields = ["userName", 'password', 'group']



class UserInfoView(APIView):

    def get(self, request):
        self.dispatch()
        user_obj = UserInfo.objects.all()
        ser = UserInforSerializer(user_obj, many=True)

        import json
        return HttpResponse(json.dumps(ser.data, ensure_ascii=False))