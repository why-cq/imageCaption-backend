from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView

from App_user.models import Users
from App_user.serializers import UsersSerializer


# Create your views here.

class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()  # 指定查询结果集
    serializer_class = UsersSerializer



class UserView2(APIView):
    serializer_class = UsersSerializer

    def get(self,request):
        print("get方法被调用了")
        return HttpResponse("success")

    def post(self,request):
        print("post方法被调用了")
        print(request.data) # 拿到接送数据
        p = UsersSerializer(data=request.data)
        p.is_valid()
        p.create(p.data)

        return HttpResponse("success")

    def delete(self,request):
        print("delete方法被调用了")
        return HttpResponse("success")