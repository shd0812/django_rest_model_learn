from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from application.models import Persons
from application.seriazalizer import PersonsSerializers
from application.seriazalizer import PersonModelSerializer
import json


# Create your views here.


class Human(View):

    def get(self, request):
        print(request.body)
        # 从数据库获取数据，结果是一个查询集 queryset
        p_set = Persons.objects.all()
        # 把从数据库获取的数据集序列化
        # ps = PersonsSerializers(p_set, many=True)
        print(p_set)
        ps = PersonModelSerializer(p_set, many=True)
        return JsonResponse(ps.data, safe=False)

    def post(self, request):
        request_data = request.body.decode("utf-8")
        import json
        # 转成python对象
        python_data = json.loads(request_data)
        # serializer_data = PersonsSerializers(data=python_data)
        serializer_data = PersonModelSerializer(data=python_data)
        try:
            # 调用 is_valid()方法来校验字典是否满足要求
            serializer_data.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer_data.errors)

        serializer_data.save()  # 因为只是给data传参数，所以会调用serializer_data.create()方法
        return JsonResponse(serializer_data.data, safe=False)


class PersonDetail(View):

    def get(self, request, id):
        p = Persons.objects.filter(pk=id).first()
        # response = PersonsSerializers(instance=p)
        response = PersonModelSerializer(instance=p)

        return JsonResponse(response.data, safe=False)

    def put(self, request, id):

        # 从接口获取传过来的数据并且序列化
        json_data = request.body.decode("utf-8")

        python_data = json.loads(json_data)
        # 从数据库获取要更新的数据
        project = Persons.objects.filter(pk=id).first()
        # serializer_data = PersonsSerializers(instance=project, data=python_data)
        serializer_data = PersonModelSerializer(instance=project, data=python_data)
        try:
            serializer_data.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer_data.errors)
        serializer_data.save()

        return JsonResponse(serializer_data.data, safe=False)

    def delete(self, request, id):
        Persons.objects.filter(pk=id).delete()

        return JsonResponse(None, safe=False, status=204)
