from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from . import models
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import Tasks
from tasks.serializers import TasksSerializer


@api_view(['GET', 'POST'])
def task_list_view(request):
    if request.method == 'GET':
        # if Tasks.DesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
def task_view(request, id):
    try:
        task = Tasks.objects.get(id = id)
    except Tasks.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TasksSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
