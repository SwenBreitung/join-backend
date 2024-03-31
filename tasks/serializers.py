from django.contrib.auth.models import Group, User
from rest_framework import serializers
from tasks.models import Task, Subtask, Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class SubtaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subtask
        fields = ['name', 'status']

       

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'color']

        
class TasksSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False) 
    subtasks = SubtaskSerializer(many=True, read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'created_at','user', 'subtasks', 'contacts']



