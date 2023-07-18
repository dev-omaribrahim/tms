import logging

from django.http import Http404
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer

# intializing logger instance
logger = logging.getLogger(__name__)


class TaskListCreateAPIView(APIView):
    """
    API endpoint for listing and creating tasks.
    """

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "status",
                openapi.IN_QUERY,
                description="Status Filter",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "priority",
                openapi.IN_QUERY,
                description="Priority Filter",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def get(self, request, format=None):
        """
        Retrieve a list of tasks based on optional filters.

        Parameters:
        - status: Filters tasks based on status.
        - priority: Filters tasks based on priority.

        Returns:
        - 200: Successful retrieval of tasks.
        - 500: Internal server error occurred.
        """
        try:
            tasks = Task.objects.all()
            task_status = request.query_params.get("status", None)
            task_priority = request.query_params.get("priority", None)

            if task_status:
                tasks = tasks.filter(status=task_status)

            if task_priority:
                tasks = tasks.filter(priority=task_priority)

            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(
                f"Something went wrong during GET method of {str(self.__class__.__name__)}: {str(e)}"
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request, format=None):
        """
        Create a new task.

        Parameters:
        - request: The request object containing task data.

        Returns:
        - 201: Task created successfully.
        - 400: Bad request, invalid data provided.
        - 500: Internal server error occurred.
        """
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(
                f"Something went wrong during the POST method of {str(self.__class__.__name__)}: {str(e)}"
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskDetailAPIView(APIView):
    """
    API endpoint for retrieving, updating, and deleting a specific task.
    """

    permission_classes = (IsAuthenticated,)

    def get_task_object(self, pk):
        """
        Get the task object based on the provided pk.

        Parameters:
        - pk: Primary key of the task.

        Returns:
        - Task object.

        Raises:
        - Http404: Task does not exist.
        """
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a specific task.

        Parameters:
        - request: The request object.
        - pk: Primary key of the task.

        Returns:
        - 200: Successful retrieval of the task.
        - 500: Internal server error occurred.
        """
        task = self.get_task_object(pk=pk)
        try:
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(
                f"Something went wrong during GET method of {str(self.__class__.__name__)}: {str(e)}"
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=TaskSerializer)
    def put(self, request, pk, format=None):
        """
        Update a specific task.

        Parameters:
        - request: The request object containing updated task data.
        - pk: Primary key of the task.

        Returns:
        - 200: Task updated successfully.
        - 400: Bad request, invalid data provided.
        - 500: Internal server error occurred.
        """
        task = self.get_task_object(pk=pk)
        try:
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(
                f"Something went wrong during the PUT method of {str(self.__class__.__name__)}: {str(e)}"
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk, format=None):
        """
        Delete a specific task.

        Parameters:
        - request: The request object.
        - pk: Primary key of the task.

        Returns:
        - 204: Task deleted successfully.
        - 500: Internal server error occurred.
        """
        task = self.get_task_object(pk=pk)
        try:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(
                f"Somthing went wrong during the DELETE method of {str(self.__class__.__name__)}: {str(e)}"
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
