from django.contrib.auth.models import Group,Permission
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
# Create your views here.

from rest_framework.views import APIView

from api.authenticator import MyAuth
from api.models import User
from api.permission import MyPermission
from api.throttle import MyThrottle


class Demo(APIView):
    def get(self,request,*args,**kwargs):
        user = User.objects.first()
        # print(user)
        # print(user.groups.first().name)
        # print(user.user_permissions.first().name)
        # print(user.email)
        group = Group.objects.first()
        # print(group)
        # print(group.user_set.first().username)
        # print(group.permissions.first())
        permission = Permission.objects.first()
        print(permission)
        # print(permission.user_set.first().username)
        per = Permission.objects.filter(pk=1).first()
        print(per.group_set.first().name)
        return Response('ok')

class BookAPIView(APIView):
    permission_classes = [MyPermission]
    authentication_classes = [MyAuth]
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response("读操作")

    def post(self, request, *args, **kwargs):
        return Response("写操作")
