from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoModel
from .serializers import TodoSerializers
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class TodoView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, pk=None):
        if pk:
            todo = get_object_or_404(TodoModel, pk=pk)
            serializers = TodoSerializers(instance=todo)
        else:
            todo = TodoModel.objects.all()
            serializers = TodoSerializers(instance=todo, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializers_data = TodoSerializers(data=request.POST)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status=status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoUpdateView(APIView):
    def put(self, request, pk=None):
        model_todo = get_object_or_404(TodoModel, pk=pk)
        serializers = TodoSerializers(instance=model_todo, data= request.POST, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        todo = TodoModel.objects.get(pk=pk)
        if todo.user != request.user:
            return Response({'Permission Denied':'You are not the owner'}, status=status.HTTP_401_UNAUTHORIZED)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

