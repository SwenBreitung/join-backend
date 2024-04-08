import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "joinbackend.settings")
django.setup()
from venv import logger
from django.conf import settings
from rest_framework.decorators import action
from django.forms import ValidationError
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TasksSerializer, SubtaskSerializer, ContactSerializer
from django.db import transaction
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import AnonymousUser
from .models import Task, Subtask, Contact


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False, url_path='refresh-tasks')
    def refresh_tasks(self, request):
        # Daten validieren
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            with transaction.atomic():
                self.queryset.delete()

                new_tasks = serializer.save()
                # Antwort mit den neu erstellten Tasks
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
           print("Validation errors:", serializer.errors)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  


