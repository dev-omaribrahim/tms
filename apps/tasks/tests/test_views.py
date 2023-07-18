import logging

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task


class TaskListCreateAPIViewTest(APITestCase):
    """
    Test cases for the TaskListCreateAPIView.
    """

    def setUp(self):
        logger = logging.getLogger("django.request")
        logger.setLevel(logging.ERROR)

        self.task1 = Task.objects.create(
            title="Task 1",
            status="pending",
            priority="high",
            description="task description",
            due_date="2023-07-01",
        )
        self.task2 = Task.objects.create(
            title="Task 2",
            status="completed",
            priority="low",
            description="task description",
            due_date="2023-07-01",
        )

    def test_get_tasks(self):
        """
        Test retrieving a list of tasks.
        """
        url = reverse("tasks:task_list_create_api_view")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_tasks_with_status_filter(self):
        """
        Test retrieving tasks with a status filter.
        """
        url = reverse("tasks:task_list_create_api_view")
        response = self.client.get(url + "?status=pending", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.task1.title)

    def test_get_tasks_with_priority_filter(self):
        """
        Test retrieving tasks with a priority filter.
        """
        url = reverse("tasks:task_list_create_api_view")
        response = self.client.get(url + "?priority=low", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.task2.title)

    def test_create_task_with_valid_data(self):
        """
        Test creating a task with valid data.
        """
        url = reverse("tasks:task_list_create_api_view")
        data = {
            "title": "New Task",
            "status": "new",
            "priority": "medium",
            "description": "task description",
            "due_date": "2023-07-01",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.get(title="New Task").priority, "medium")

    def test_create_task_with_invalid_data(self):
        """
        Test creating a task with invalid data.
        """
        url = reverse("tasks:task_list_create_api_view")
        invalid_data_list = [
            {
                "title": "",
                "status": "pending",
                "priority": "medium",
                "description": "task description",
                "due_date": "2023-07-01",
            },
            {
                "title": "task",
                "status": "",
                "priority": "medium",
                "description": "task description",
                "due_date": "2023-07-01",
            },
            {
                "title": "task",
                "status": "pending",
                "priority": "",
                "description": "task description",
                "due_date": "2023-07-01",
            },
            {
                "title": "task",
                "status": "pending",
                "priority": "medium",
                "description": "",
                "due_date": "2023-07-01",
            },
            {
                "title": "task",
                "status": "pending",
                "priority": "medium",
                "description": "task description",
                "due_date": "",
            },
        ]
        for data in invalid_data_list:
            response = self.client.post(url, data, format="json")

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Task.objects.count(), 2)


class TaskDetailAPIViewTest(APITestCase):
    """
    Test cases for the TaskDetailAPIView.
    """

    def setUp(self):
        logger = logging.getLogger("django.request")
        logger.setLevel(logging.ERROR)

        self.task = Task.objects.create(
            title="Existing Task",
            status="pending",
            priority="high",
            description="task description",
            due_date="2023-07-01",
        )

    def test_get_task(self):
        """
        Test retrieving a specific task.
        """
        url = reverse("tasks:task_detail_api_view", args=[self.task.pk])
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task.title)

    def test_update_task_with_valid_data(self):
        """
        Test updating a specific task with valid data.
        """
        url = reverse("tasks:task_detail_api_view", args=[self.task.pk])
        data = {
            "title": "Updated Task",
            "status": "completed",
            "priority": "low",
            "description": "task description",
            "due_date": "2023-07-01",
        }
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(pk=self.task.pk).title, "Updated Task")
        self.assertEqual(Task.objects.get(pk=self.task.pk).status, "completed")

    def test_update_task_with_invalid_data(self):
        """
        Test updating a specific task with invalid data.
        """
        url = reverse("tasks:task_detail_api_view", args=[self.task.pk])
        data = {"title": "", "status": "completed", "priority": "low"}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(Task.objects.get(pk=self.task.pk).title, "")

    def test_delete_task(self):
        """
        Test deleting a specific task.
        """
        url = reverse("tasks:task_detail_api_view", args=[self.task.pk])
        response = self.client.delete(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
