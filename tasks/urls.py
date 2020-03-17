from django.urls import path
from .viewsets import task_view, task_list_view

# REST FRAMEWORK URLS

urlpatterns = [
    path('create/', task_list_view, name='task_insert'),   #post
    path('<int:id>/', task_view, name="task_update"),  #update
    path('list/', task_list_view, name="task_list") #get
]
