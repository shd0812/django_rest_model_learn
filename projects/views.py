from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse
from projects.models import Projects
from projects.seriazalizer import  ProjectModelSerializer
import json
# Create your views here.


class ProjectView(View):

    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectModelSerializer(instance=projects, many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        # 获取接口传过来的数据
        request_data = request.body.decode('utf-8')
        python_data = json.loads(request_data)
        # 序列化
        serializer = ProjectModelSerializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.validated_data, safe=False)

class ProjectsDetail(View):
    def get(self, request, id):
        projects = Projects.objects.filter(pk=id).first()
        print(projects)
        if projects is None:
            return JsonResponse({"code": 404, "error_message": "没有找到项目"})
        # 序列化
        serializer = ProjectModelSerializer(instance=projects)
        return JsonResponse(serializer.data, safe=False)


    def put(self, request, id):
        projects = Projects.objects.filter(pk=id).first()
        # 获取接口传过来的数据
        request_data = request.body.decode('utf-8')
        python_data = json.loads(request_data)
        serializer = ProjectModelSerializer(instance=projects, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializer.errors, safe=False)
        serializer.save()
        return JsonResponse(serializer.validated_data, safe=False)

    def delete(self, request, id):
        projects = Projects.objects.filter(pk=id).delete()
        return JsonResponse(None, safe=False)

