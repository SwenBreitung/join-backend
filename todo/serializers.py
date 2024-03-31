from django.contrib.auth.models import Group, User
from rest_framework import serializers

from todo.models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','username','email']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    title = serializers.CharField(required=False)  # Optional machen
    text = serializers.CharField(required=False)  # Optional machen
    class Meta:
        model = Todo
        fields = ['id','title', 'text', 'created_at','user','time_past']

       