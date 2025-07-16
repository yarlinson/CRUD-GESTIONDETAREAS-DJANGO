from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created', 'datecompleted', 'important']
    ordering = ['-created']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.datecompleted = timezone.now()
        task.save()
        return Response({'status': 'task completed'})

    @action(detail=False)
    def completed(self, request):
        tasks = Task.objects.filter(
            user=request.user,
            datecompleted__isnull=False
        )
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def pending(self, request):
        tasks = Task.objects.filter(
            user=request.user,
            datecompleted__isnull=True
        )
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data) 