from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pageapp import serializer
from pageapp import models
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# Create your views here.
from pageapp.models import Company, Phone


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2

    # Client can control the page using this query parameter.
    page_query_param = 'page'

    page_size_query_param = "size"

    max_page_size = 4

class MyLimitPageNumberPagination(LimitOffsetPagination):
    default_limit = "2"
    limit_query_param = 'limit'
    limit_query_description =('Number of results to return per page.')
    offset_query_param = 'offset'
    max_page_size = 4


class PageView(APIView):

    def get(self, request, *args, **kwargs):
        silks = models.Silk.objects.all()
        pages = MyLimitPageNumberPagination()
        page_data = pages.paginate_queryset(silks, request, self)
        ser = serializer.SilkSerializer(instance=page_data, many=True)
        print(pages.get_next_link())
        print(pages.to_html())
        return pages.get_paginated_response(ser.data)
        # return Response(ser.data)

class ModelView( ModelViewSet):

    queryset = models.Silk.objects.all()
    serializer_class = serializer.SilkSerializer
    pagination_class =  MyLimitPageNumberPagination
    # +7qJ)aJYY>KD
    #run -itd --name mysql -p 3306:3306 --restart=always -e MYSQL_ROOT_PASSWORD=123 mysql:5.7
    def list(self, request, *args, **kwargs):
        '''获取最后一条记录'''

        # 获取模型数据
        book = self.get_queryset()
        s = self.get_serializer(book, many=True)
        return Response(s.data)
    @action(detail=False)
    def names(self, request):
        book = self.get_queryset()
        s = self.get_serializer(book, many=True)
        return Response(s.data)
    # def create(self, request, *args, **kwargs):
    #     ser = self.get_serializer(data=request.data)
    #
    #     ser.is_valid(raise_exception=True)
    #
    #     # ser.save()
    #     return Response("...")
    #
    #
    #     return Response(s.data)

class PhoneView(APIView):

    def get(self, request, *args, **kwargs):
        # phone = request._request.GET.get("phone")
        company = request._request.GET.get("company")
        print(company)
        cc = Company.objects.filter(com_name="三星公司").first()
        print(cc.phone_set.price)
        print(type(cc.phone_set))
        p =Phone.objects.filter(company__com_name="苹果公司").first()

        return  Response(f"{p.phone_name}")