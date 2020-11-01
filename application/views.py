from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from application.models import Persons
from application.seriazalizer import PersonsSerializers


# Create your views here.


class Human(View):

    def get(self, request):
        print(request.body)
        # 从数据库获取数据，结果是一个查询集 queryset
        p_set = Persons.objects.all()
        # 把从数据库获取的数据集序列化
        ps = PersonsSerializers(p_set, many=True)
        # l = []
        # for p in p_set:
        #     dic = {}
        #     dic['id'] = p.pk
        #     dic['name'] = p.name
        #     dic['phone'] = p.phone
        #     # dic['sex'] = p.sex
        #     dic['address'] = p.address
        #     l.append(dic)
        # 返回结果
        return JsonResponse(ps.data, safe=False)

    def post(self, request):
        print(request.headers)
        # decode  byte 转str
        # 获取用户请求过来的数据
        request_data = request.body.decode("utf-8")
        import json
        # 转成python对象
        python_data = json.loads(request_data)
        # 把python_data反序列化后，使用序列化来做一些校验
        # 如果在创造序列化器对象的时候只给data传参数，那么调用save()方法，实际调用的
        # 就是序列化器对象的create方法
        serializer_data = PersonsSerializers(data=python_data)
        try:  # 调用 is_valid()方法来校验字典是否满足要求
            serializer_data.is_valid(raise_exception=True)
        except Exception as  e:
            return JsonResponse(serializer_data.errors)
        # # 调用Persons model类直接创建对象
        # p = Persons.objects.create(**serializer_data.validated_data)

        # 不建议操作model的方法直接在view调用，建议去序列化里操作，因此如此改造
        serializer_data.save()  # 因为只是给data传参数，所以会调用serializer_data.create()方法
        return JsonResponse(serializer_data.data, safe=False)


class PersonDetail(View):

    def get(self, request, id):
        p = Persons.objects.filter(pk=id).first()
        response = PersonsSerializers(instance=p)

        return JsonResponse(response.data, safe=False)

    def put(self, request, id):

        # 从接口获取传过来的数据并且序列化
        json_data = request.body.decode("utf-8")
        import json
        python_data = json.loads(json_data)
        # 从数据库获取要更新的数据
        project = Persons.objects.filter(pk=id).first()
        # 在创建序列化对象时，如果同时给instance和data传参， 那么调用save()方法，
        # 会去调用序列化对象的update()方法
        serializer_data = PersonsSerializers(instance=project, data=python_data)
        try:
            serializer_data.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            return JsonResponse(serializer_data.errors)
        serializer_data.save()
        # project.name = serializer_data.validated_data['name']
        # project.phone = serializer_data.validated_data['phone']
        # project.address = serializer_data.validated_data['address']
        # project.save()
        # seriazer = PersonsSerializers(instance=p)
        # print("seriazer：{}, 类型是{}".format(seriazer, type(seriazer)))

        return JsonResponse(serializer_data.data, safe=False)

    def delete(self, request, id):
        person = Persons.objects.filter(pk=id).delete()

        return JsonResponse(None, safe=False, status=204)
