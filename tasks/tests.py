from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .serializers import TasksSerializer

from .models import Tasks


# from .serializers import TaskSerializers

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_task(title="", created_at=""):
        if title != "":
            Tasks.objects.create(title=title, checked=False, createdAt=created_at)

    def setUp(self):
        # add test data
        self.create_task("Make a todo app", "","")
        self.create_task("Get water","","")

class GetAllSongsTest(BaseViewTest):

    def test_get_all_song(self):
        response = self.client.get(
            reverse("task-all")
        )

    expected = Tasks.objects.all()
    serialized = TasksSerializer(expected, many = True)

