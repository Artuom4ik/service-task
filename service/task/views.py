from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TaskSerializer
from .permissions import IsClient, IsEmployee
from .models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsClient | IsEmployee]

        elif self.action == 'create':
            permission_classes = [IsClient]

        elif self.action == 'update':
            permission_classes = [IsClient | IsEmployee]

        elif self.action == 'close':
            permission_classes = [IsEmployee]

        elif self.action == 'retrieve':
            permission_classes = [IsClient | IsEmployee]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def list(self, serializer):
        if self.request.user.role == 'client':
            tasks = Task.objects.filter(client=self.request.user)

        else:
            tasks = Task.objects.all()

        serializer = serializer(tasks, many=True)

        return Response(serializer.data)

    def create(self, serializer):
        serializer = serializer.save(client=self.request.user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        instance = get_object_or_404(Task, pk=pk)

        serializer = self.get_serializer(instance, data=request.data)
        serializer.save()

        return Response({"Update task": serializer.data})

    def retrieve(self, request, pk=None):
        if not pk:
            return Response({"error": "Method GET not allowed"})

        task = get_object_or_404(Task, pk=pk)

        if self.request.user.role == 'client':
            if task.client != self.request.user:
                return Response({"error": "Method GET not allowed"})

        serializer = self.get_serializer(task)

        return Response({"Task": serializer.data})
