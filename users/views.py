from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

from users.auth import VipAuthTicate
from users.permission import myPermission
from users.my_throttling import UserThrottling
from users.models import UserInfo, UserToken

import json
import hashlib
import time
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

result = {
    "code": 200,
    "msg": "success",
    "data": [
        {"user": "shd"},
        {"user": "myj"},
        {"user": "zhoul"}
    ]
}


def md5(userName):
    cttime = time.time()

    md = hashlib.md5("shd".encode("utf-8"))
    md.update(str(cttime).encode("utf-8"))
    return md.hexdigest()


# Create your views here.

class UserInfoView(APIView):
    authentication_classes = []   # 认证
    permission_classes = []      #授权

    def get(self, request, *args):

        return JsonResponse([1, 2, 3], safe=False)

    def post(self, request):
        ret = {
            "code": "1000",
            "msg": None
        }
        try:
            request_body = request.body.decode('utf-8')

            python_data = json.loads(request_body)
            userName, passWord = python_data.get("userName"), python_data.get("passWord")
            obj = UserInfo.objects.filter(userName=userName, password=passWord).first()

            if obj:
                ret['code'] = 200
                ret['msg'] = "恭喜登录成功"
                token = md5(userName)
                UserToken.objects.update_or_create(user=obj, defaults={"token": token})
                ret['data'] = {
                    "user": obj.userName
                }
                ret['token'] = token
                return JsonResponse(ret)
            ret['code'] = 400
            ret['msg'] = "账号或密码不对"
            return JsonResponse(ret)
        except Exception:
            ret['message'] = "服务器开小差了"
            return JsonResponse(ret)


class OrderView(APIView):
    authentication_classes = [VipAuthTicate, ]
    permission_classes = [myPermission, ]
    throttle_classes = [UserThrottling, ]

    def get(self, request):
        self.dispatch()
        print(request.user.userType)

        return JsonResponse(result)


from rest_framework.versioning import BaseVersioning, QueryParameterVersioning, URLPathVersioning


# a 版本类   自定义  http://127.0.0.1:8000/api/users/userList/?version=v1
# class ParamVersion(BaseVersioning):
#     def determine_version(self, request, *args, **kwargs):
#         versions = request.query_params.get('version')
#         return versions
#
#
# class UserView(APIView):
#     # versioning_class = [ParamVersion, ]
#     versioning_class = ParamVersion
#
#     def get(self, request, *args, **kwargs):
#         # 获取版本
#         # version = request.query_params.get("version")
#         # print(version)
#         print(request.version)
#         return HttpResponse("用户列表")


class UserView(APIView):
    # versioning_class = QueryParameterVersioning  # 使用封装的 http://127.0.0.1:8000/api/users/userList/?version=v1
    #versioning_class = URLPathVersioning  # 使用封装的 http://127.0.0.1:8000/api/users/v1/userList/

    def get(self, request, *args, **kwargs):
        # 获取版本
        # version = request.query_params.get("version")
        # print(version)
        print(request.version)
        return HttpResponse("用户列表")

