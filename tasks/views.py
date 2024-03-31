from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TasksSerializer, SubtaskSerializer, ContactSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    def create(self, request, *args, **kwargs):
        task_data = request.data.copy()

        subtasks_data = task_data.pop('subtasks', None)
        contacts_data = task_data.pop('contacts', None)

        task = self.create_task(task_data)
        self.process_subtasks(subtasks_data, task)
        self.process_contacts(contacts_data, task)

        task_serializer = self.get_serializer(task)
        return Response(task_serializer.data, status=status.HTTP_201_CREATED)


    def create_task(self, task_data):
        task_serializer = self.get_serializer(data=task_data)
        task_serializer.is_valid(raise_exception=True)
        return task_serializer.save(user=self.request.user)


    def process_subtasks(self, subtasks_data, task):
        if subtasks_data is None:
            return
        for subtask_data in subtasks_data:
            subtask_data['task'] = task.id
            subtask_serializer = SubtaskSerializer(data=subtask_data)
            subtask_serializer.is_valid(raise_exception=True)
            subtask_serializer.save()


    def process_contacts(self, contacts_data, task):
        if contacts_data is None:
            return
        for contact_data in contacts_data:
            contact_data['task'] = task.id
            contact_serializer = ContactSerializer(data=contact_data)
            contact_serializer.is_valid(raise_exception=True)
            contact_serializer.save()


