from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer
# Create your views here.

class UserRegisterView(APIView):
    def post(self, request):
        serializers = UserRegisterSerializer(data=request.POST)
        if serializers.is_valid():
            User.objects.create_user(
                username=serializers.validated_data['username'],
                email=serializers.validated_data['email'],
                password=serializers.validated_data['password'],
            )
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
