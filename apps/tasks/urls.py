from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListCreateAPIView.as_view(), name="task_list_create_api_view"),
    path("<int:pk>/", views.TaskDetailAPIView.as_view(), name="task_detail_api_view"),
]
