from django.test import TestCase

from ..serializers import TaskSerializer


class TaskSerializerTest(TestCase):
    """
    Test cases for the TaskSerializer.
    """

    def test_task_serializer_valid_data(self):
        """
        Test the serializer with valid data.
        """
        task_data = {
            "title": "New Task",
            "status": "new",
            "priority": "high",
            "description": "task description",
            "due_date": "2023-07-01",
        }
        serializer = TaskSerializer(data=task_data)
        serializer.is_valid()
        self.assertTrue(serializer.is_valid())

    def test_task_serializer_missing_title(self):
        """
        Test the serializer with missing title field.
        """
        task_data = {
            "status": "new",
            "priority": "high",
            "description": "task description",
            "due_date": "2023-07-01",
        }
        serializer = TaskSerializer(data=task_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["title"][0], "This field is required.")

    def test_task_serializer_invalid_status(self):
        """
        Test the serializer with invalid status field.
        """
        task_data = {
            "title": "New Task",
            "priority": "high",
            "description": "task description",
            "due_date": "2023-07-01",
        }
        serializer = TaskSerializer(data=task_data)
        self.assertFalse(serializer.is_valid())

    def test_task_serializer_invalid_priority(self):
        """
        Test the serializer with invalid priority field.
        """
        task_data = {
            "title": "New Task",
            "status": "new",
            "description": "task description",
            "due_date": "2023-07-01",
        }
        serializer = TaskSerializer(data=task_data)
        self.assertFalse(serializer.is_valid())

    def test_task_serializer_create(self):
        """
        Test creating a task using the serializer.
        """
        task_data = {
            "title": "New Task",
            "status": "new",
            "priority": "high",
            "description": "task description",
            "due_date": "2023-07-01",
        }
        serializer = TaskSerializer(data=task_data)
        self.assertTrue(serializer.is_valid())

        task = serializer.save()

        self.assertEqual(task.title, "New Task")
        self.assertEqual(task.status, "new")
        self.assertEqual(task.priority, "high")
