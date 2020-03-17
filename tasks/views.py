from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Tasks
from .serializers import TasksSerializer

# Get all the employees
def post():
    form = Tasks(Request.POST)
    if form.is_value():
        url = form.clean_data['url']

class TaskList(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    def get(self, request):
        task = Tasks.objects.all()
        serializer = TasksSerializer(task, many=True)
        return Response(serializer.data)

    def post(self):
        print("POST")


    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


