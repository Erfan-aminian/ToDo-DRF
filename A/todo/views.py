from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoModel
from .serializers import TodoSerializers

# Create your views here.

class TodoView(APIView):
    def get(self, request):
        todo = TodoModel.objects.all()
        serializers = TodoSerializers(instance=todo, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializers_data = TodoSerializers(data=request.POST)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status=status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)


